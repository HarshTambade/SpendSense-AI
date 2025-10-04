'use client';

import { useState, useEffect } from 'react';
import { apiClient } from '@/lib/api/client';
import { Expense, ExpenseStatus, RiskLevel } from '@/lib/api/types';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Badge } from '@/components/ui/badge';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/components/ui/table';
import { Dialog, DialogContent, DialogDescription, DialogHeader, DialogTitle } from '@/components/ui/dialog';
import { Textarea } from '@/components/ui/textarea';
import { Label } from '@/components/ui/label';
import { CheckCircle, XCircle, Clock, AlertTriangle, Shield, TrendingUp } from 'lucide-react';
import { toast } from 'sonner';

interface PendingApproval {
  approval: any;
  expense: Expense;
  submitter: any;
}

export default function ManagerDashboard() {
  const [pendingApprovals, setPendingApprovals] = useState<PendingApproval[]>([]);
  const [teamExpenses, setTeamExpenses] = useState<Expense[]>([]);
  const [selectedExpense, setSelectedExpense] = useState<PendingApproval | null>(null);
  const [isDialogOpen, setIsDialogOpen] = useState(false);
  const [comments, setComments] = useState('');
  const [riskData, setRiskData] = useState<any>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    fetchPendingApprovals();
    fetchTeamExpenses();
  }, []);

  const fetchPendingApprovals = async () => {
    const response = await apiClient.get<PendingApproval[]>('/approvals/pending');
    if (response.data) {
      setPendingApprovals(response.data);
    }
    setIsLoading(false);
  };

  const fetchTeamExpenses = async () => {
    const response = await apiClient.get<Expense[]>('/expenses/');
    if (response.data) {
      setTeamExpenses(response.data);
    }
  };

  const fetchRiskScore = async (expenseId: number) => {
    const response = await apiClient.get<any>(`/expenses/${expenseId}/risk`);
    if (response.data) {
      setRiskData(response.data);
    }
  };

  const handleApprovalAction = async (approvalId: number, status: 'approved' | 'rejected') => {
    const response = await apiClient.put(`/approvals/${approvalId}`, {
      status,
      comments
    });

    if (response.data) {
      toast.success(`Expense ${status}!`);
      setIsDialogOpen(false);
      setComments('');
      setSelectedExpense(null);
      fetchPendingApprovals();
      fetchTeamExpenses();
    } else {
      toast.error(response.error || 'Action failed');
    }
  };

  const openApprovalDialog = async (approval: PendingApproval) => {
    setSelectedExpense(approval);
    await fetchRiskScore(approval.expense.id);
    setIsDialogOpen(true);
  };

  const getRiskBadge = (level: RiskLevel) => {
    switch (level) {
      case RiskLevel.HIGH:
        return <Badge className="bg-red-100 text-red-800"><AlertTriangle className="h-3 w-3 mr-1" />High Risk</Badge>;
      case RiskLevel.MEDIUM:
        return <Badge className="bg-yellow-100 text-yellow-800"><AlertTriangle className="h-3 w-3 mr-1" />Medium Risk</Badge>;
      default:
        return <Badge className="bg-green-100 text-green-800"><Shield className="h-3 w-3 mr-1" />Low Risk</Badge>;
    }
  };

  const getStatusBadge = (status: ExpenseStatus) => {
    switch (status) {
      case ExpenseStatus.APPROVED:
        return <Badge className="bg-green-100 text-green-800"><CheckCircle className="h-3 w-3 mr-1" />Approved</Badge>;
      case ExpenseStatus.REJECTED:
        return <Badge className="bg-red-100 text-red-800"><XCircle className="h-3 w-3 mr-1" />Rejected</Badge>;
      default:
        return <Badge className="bg-yellow-100 text-yellow-800"><Clock className="h-3 w-3 mr-1" />Pending</Badge>;
    }
  };

  if (isLoading) {
    return <div className="text-center py-8">Loading...</div>;
  }

  return (
    <div className="space-y-6">
      {/* Stats */}
      <div className="grid md:grid-cols-3 gap-4">
        <Card>
          <CardHeader className="pb-2">
            <CardDescription>Pending Approvals</CardDescription>
            <CardTitle className="text-3xl text-yellow-600">{pendingApprovals.length}</CardTitle>
          </CardHeader>
        </Card>
        <Card>
          <CardHeader className="pb-2">
            <CardDescription>Team Expenses</CardDescription>
            <CardTitle className="text-3xl">{teamExpenses.length}</CardTitle>
          </CardHeader>
        </Card>
        <Card>
          <CardHeader className="pb-2">
            <CardDescription>Approved This Month</CardDescription>
            <CardTitle className="text-3xl text-green-600">
              {teamExpenses.filter(e => e.status === ExpenseStatus.APPROVED).length}
            </CardTitle>
          </CardHeader>
        </Card>
      </div>

      {/* Pending Approvals */}
      <Card>
        <CardHeader>
          <CardTitle>Pending Approvals</CardTitle>
          <CardDescription>Review and approve team expenses with AI risk scores</CardDescription>
        </CardHeader>
        <CardContent>
          {pendingApprovals.length === 0 ? (
            <div className="text-center py-8 text-slate-500">
              <CheckCircle className="h-12 w-12 mx-auto mb-2 text-green-500" />
              <p>All caught up! No pending approvals.</p>
            </div>
          ) : (
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Employee</TableHead>
                  <TableHead>Date</TableHead>
                  <TableHead>Description</TableHead>
                  <TableHead>Amount</TableHead>
                  <TableHead>Category</TableHead>
                  <TableHead>Action</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {pendingApprovals.map((approval) => (
                  <TableRow key={approval.approval.id}>
                    <TableCell className="font-medium">{approval.submitter.full_name}</TableCell>
                    <TableCell>{new Date(approval.expense.expense_date).toLocaleDateString()}</TableCell>
                    <TableCell className="max-w-xs truncate">{approval.expense.description}</TableCell>
                    <TableCell>{approval.expense.currency} {approval.expense.amount.toFixed(2)}</TableCell>
                    <TableCell className="capitalize">{approval.expense.category.replace('_', ' ')}</TableCell>
                    <TableCell>
                      <Button size="sm" onClick={() => openApprovalDialog(approval)}>
                        Review
                      </Button>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          )}
        </CardContent>
      </Card>

      {/* Team Expenses */}
      <Card>
        <CardHeader>
          <CardTitle>Team Expenses</CardTitle>
          <CardDescription>All expenses from your team</CardDescription>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Employee</TableHead>
                <TableHead>Date</TableHead>
                <TableHead>Description</TableHead>
                <TableHead>Amount</TableHead>
                <TableHead>Status</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {teamExpenses.slice(0, 10).map((expense) => (
                <TableRow key={expense.id}>
                  <TableCell>Employee #{expense.user_id}</TableCell>
                  <TableCell>{new Date(expense.expense_date).toLocaleDateString()}</TableCell>
                  <TableCell className="max-w-xs truncate">{expense.description}</TableCell>
                  <TableCell>{expense.currency} {expense.amount.toFixed(2)}</TableCell>
                  <TableCell>{getStatusBadge(expense.status)}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>

      {/* Approval Dialog */}
      {selectedExpense && (
        <Dialog open={isDialogOpen} onOpenChange={setIsDialogOpen}>
          <DialogContent className="max-w-2xl">
            <DialogHeader>
              <DialogTitle>Review Expense</DialogTitle>
              <DialogDescription>Submitted by {selectedExpense.submitter.full_name}</DialogDescription>
            </DialogHeader>

            <div className="space-y-4">
              {/* Expense Details */}
              <div className="grid md:grid-cols-2 gap-4">
                <div>
                  <Label className="text-slate-600">Amount</Label>
                  <p className="text-lg font-semibold">
                    {selectedExpense.expense.currency} {selectedExpense.expense.amount.toFixed(2)}
                  </p>
                </div>
                <div>
                  <Label className="text-slate-600">Category</Label>
                  <p className="text-lg font-semibold capitalize">
                    {selectedExpense.expense.category.replace('_', ' ')}
                  </p>
                </div>
                <div>
                  <Label className="text-slate-600">Date</Label>
                  <p className="text-lg font-semibold">
                    {new Date(selectedExpense.expense.expense_date).toLocaleDateString()}
                  </p>
                </div>
                <div>
                  <Label className="text-slate-600">Vendor</Label>
                  <p className="text-lg font-semibold">{selectedExpense.expense.vendor || 'N/A'}</p>
                </div>
              </div>

              <div>
                <Label className="text-slate-600">Description</Label>
                <p className="text-base">{selectedExpense.expense.description}</p>
              </div>

              {/* AI Risk Score */}
              {riskData && (
                <Card className="bg-slate-50">
                  <CardHeader>
                    <div className="flex items-center justify-between">
                      <CardTitle className="text-lg">AI Risk Analysis</CardTitle>
                      {getRiskBadge(riskData.risk_level)}
                    </div>
                  </CardHeader>
                  <CardContent className="space-y-2">
                    <div className="flex items-center gap-2">
                      <Shield className="h-5 w-5 text-blue-600" />
                      <span className="font-semibold">Risk Score: {riskData.score}/100</span>
                    </div>
                    <p className="text-sm text-slate-600">{riskData.message}</p>
                    {riskData.factors && riskData.factors.length > 0 && (
                      <div className="mt-2">
                        <Label className="text-xs text-slate-600">Risk Factors:</Label>
                        <ul className="list-disc list-inside text-sm text-slate-700">
                          {riskData.factors.map((factor: string, idx: number) => (
                            <li key={idx}>{factor}</li>
                          ))}
                        </ul>
                      </div>
                    )}
                  </CardContent>
                </Card>
              )}

              {/* Comments */}
              <div className="space-y-2">
                <Label htmlFor="comments">Comments (Optional)</Label>
                <Textarea
                  id="comments"
                  placeholder="Add comments for the employee..."
                  value={comments}
                  onChange={(e) => setComments(e.target.value)}
                />
              </div>

              {/* Actions */}
              <div className="flex gap-3">
                <Button
                  className="flex-1 bg-green-600 hover:bg-green-700"
                  onClick={() => handleApprovalAction(selectedExpense.approval.id, 'approved')}
                >
                  <CheckCircle className="h-4 w-4 mr-2" />
                  Approve
                </Button>
                <Button
                  className="flex-1 bg-red-600 hover:bg-red-700"
                  onClick={() => handleApprovalAction(selectedExpense.approval.id, 'rejected')}
                >
                  <XCircle className="h-4 w-4 mr-2" />
                  Reject
                </Button>
              </div>
            </div>
          </DialogContent>
        </Dialog>
      )}
    </div>
  );
}
