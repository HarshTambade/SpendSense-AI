'use client';

import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Badge } from "@/components/ui/badge";
import Link from "next/link";
import { 
  ArrowRight, 
  Brain, 
  Shield, 
  TrendingUp, 
  Zap, 
  CheckCircle2,
  BarChart3,
  FileText,
  Users,
  Globe,
  Sparkles,
  Lock,
  Clock,
  DollarSign
} from "lucide-react";

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-50 to-white">
      {/* Navigation */}
      <nav className="border-b bg-white/80 backdrop-blur-sm sticky top-0 z-50">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-2">
              <div className="w-10 h-10 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-lg flex items-center justify-center">
                <Sparkles className="w-6 h-6 text-white" />
              </div>
              <span className="text-2xl font-bold bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
                SpendSense AI
              </span>
            </div>
            <div className="flex items-center space-x-4">
              <Link href="/login">
                <Button variant="ghost" className="text-slate-700">
                  Sign In
                </Button>
              </Link>
              <Link href="/signup">
                <Button className="bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700">
                  Get Started
                  <ArrowRight className="ml-2 w-4 h-4" />
                </Button>
              </Link>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section className="container mx-auto px-4 py-20">
        <div className="text-center max-w-4xl mx-auto">
          <Badge className="mb-4 bg-blue-100 text-blue-700 hover:bg-blue-100">
            <Sparkles className="w-3 h-3 mr-1" />
            AI-Powered Expense Management
          </Badge>
          <h1 className="text-5xl md:text-6xl font-bold mb-6 bg-gradient-to-r from-slate-900 via-blue-800 to-indigo-900 bg-clip-text text-transparent leading-tight">
            Smart Expense Management
            <br />
            Powered by AI
          </h1>
          <p className="text-xl text-slate-600 mb-8 leading-relaxed">
            Transform your expense workflow with intelligent automation, real-time insights,
            and AI-powered fraud detection. Save time, reduce costs, and make smarter decisions.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link href="/signup">
              <Button size="lg" className="bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 text-lg px-8">
                Start Free Trial
                <ArrowRight className="ml-2 w-5 h-5" />
              </Button>
            </Link>
            <Button size="lg" variant="outline" className="text-lg px-8">
              Watch Demo
            </Button>
          </div>
          <p className="text-sm text-slate-500 mt-4">
            No credit card required • 14-day free trial • Cancel anytime
          </p>
        </div>

        {/* Hero Image/Dashboard Preview */}
        <div className="mt-16 relative">
          <div className="absolute inset-0 bg-gradient-to-t from-white via-transparent to-transparent z-10"></div>
          <div className="rounded-2xl border-4 border-slate-200 shadow-2xl overflow-hidden bg-white">
            <div className="bg-gradient-to-r from-blue-600 to-indigo-600 p-3 flex items-center space-x-2">
              <div className="flex space-x-1.5">
                <div className="w-3 h-3 rounded-full bg-red-400"></div>
                <div className="w-3 h-3 rounded-full bg-yellow-400"></div>
                <div className="w-3 h-3 rounded-full bg-green-400"></div>
              </div>
              <div className="flex-1 text-center text-white text-sm font-medium">
                SpendSense AI Dashboard
              </div>
            </div>
            <div className="p-8 bg-gradient-to-br from-slate-50 to-blue-50">
              <div className="grid grid-cols-4 gap-4 mb-6">
                <Card className="bg-white border-blue-200">
                  <CardContent className="p-4">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-sm text-slate-600">Total Spend</span>
                      <DollarSign className="w-4 h-4 text-blue-600" />
                    </div>
                    <div className="text-2xl font-bold text-slate-900">$124.5K</div>
                    <div className="text-xs text-green-600 flex items-center mt-1">
                      <TrendingUp className="w-3 h-3 mr-1" />
                      12% vs last month
                    </div>
                  </CardContent>
                </Card>
                <Card className="bg-white border-indigo-200">
                  <CardContent className="p-4">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-sm text-slate-600">Pending</span>
                      <Clock className="w-4 h-4 text-indigo-600" />
                    </div>
                    <div className="text-2xl font-bold text-slate-900">23</div>
                    <div className="text-xs text-slate-500 mt-1">Awaiting approval</div>
                  </CardContent>
                </Card>
                <Card className="bg-white border-green-200">
                  <CardContent className="p-4">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-sm text-slate-600">Approved</span>
                      <CheckCircle2 className="w-4 h-4 text-green-600" />
                    </div>
                    <div className="text-2xl font-bold text-slate-900">156</div>
                    <div className="text-xs text-slate-500 mt-1">This month</div>
                  </CardContent>
                </Card>
                <Card className="bg-white border-red-200">
                  <CardContent className="p-4">
                    <div className="flex items-center justify-between mb-2">
                      <span className="text-sm text-slate-600">Risk Alerts</span>
                      <Shield className="w-4 h-4 text-red-600" />
                    </div>
                    <div className="text-2xl font-bold text-slate-900">3</div>
                    <div className="text-xs text-red-600 mt-1">Requires attention</div>
                  </CardContent>
                </Card>
              </div>
              <div className="h-48 bg-white rounded-lg border border-slate-200 flex items-center justify-center">
                <BarChart3 className="w-16 h-16 text-slate-300" />
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20 bg-slate-50">
        <div className="container mx-auto px-4">
          <div className="text-center mb-16">
            <Badge className="mb-4 bg-indigo-100 text-indigo-700">Features</Badge>
            <h2 className="text-4xl font-bold mb-4 text-slate-900">
              Everything you need to manage expenses
            </h2>
            <p className="text-xl text-slate-600 max-w-2xl mx-auto">
              Powerful features designed to streamline your expense management workflow
            </p>
          </div>

          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {[
              {
                icon: Brain,
                title: "AI-Powered Insights",
                description: "Get intelligent recommendations and spending patterns analysis powered by advanced machine learning",
                color: "blue"
              },
              {
                icon: Shield,
                title: "Fraud Detection",
                description: "Real-time risk scoring and anomaly detection to protect your business from fraudulent expenses",
                color: "red"
              },
              {
                icon: FileText,
                title: "OCR Receipt Scanning",
                description: "Automatically extract data from receipts using advanced optical character recognition",
                color: "green"
              },
              {
                icon: Zap,
                title: "Instant Approvals",
                description: "Multi-level approval workflows with smart routing and automated notifications",
                color: "yellow"
              },
              {
                icon: BarChart3,
                title: "Real-Time Analytics",
                description: "Interactive dashboards with spending insights, trends, and customizable reports",
                color: "purple"
              },
              {
                icon: Globe,
                title: "Multi-Currency Support",
                description: "Automatic currency conversion with real-time exchange rates for global teams",
                color: "cyan"
              }
            ].map((feature, index) => (
              <Card key={index} className="border-2 hover:border-blue-300 transition-all hover:shadow-lg bg-white">
                <CardContent className="p-6">
                  <div className={`w-12 h-12 rounded-lg bg-${feature.color}-100 flex items-center justify-center mb-4`}>
                    <feature.icon className={`w-6 h-6 text-${feature.color}-600`} />
                  </div>
                  <h3 className="text-xl font-semibold mb-2 text-slate-900">{feature.title}</h3>
                  <p className="text-slate-600">{feature.description}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Benefits Section */}
      <section className="py-20">
        <div className="container mx-auto px-4">
          <div className="grid lg:grid-cols-2 gap-12 items-center">
            <div>
              <Badge className="mb-4 bg-green-100 text-green-700">Benefits</Badge>
              <h2 className="text-4xl font-bold mb-6 text-slate-900">
                Why teams choose SpendSense AI
              </h2>
              <div className="space-y-4">
                {[
                  "Save 10+ hours per week on expense processing",
                  "Reduce expense fraud by up to 80%",
                  "Get real-time visibility into company spending",
                  "Automate approval workflows and notifications",
                  "Generate compliance-ready reports instantly",
                  "Scale effortlessly as your team grows"
                ].map((benefit, index) => (
                  <div key={index} className="flex items-start space-x-3">
                    <CheckCircle2 className="w-6 h-6 text-green-600 flex-shrink-0 mt-0.5" />
                    <span className="text-lg text-slate-700">{benefit}</span>
                  </div>
                ))}
              </div>
              <Link href="/signup">
                <Button size="lg" className="mt-8 bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700">
                  Get Started Now
                  <ArrowRight className="ml-2 w-5 h-5" />
                </Button>
              </Link>
            </div>
            <div className="grid grid-cols-2 gap-6">
              <Card className="bg-gradient-to-br from-blue-50 to-indigo-50 border-blue-200">
                <CardContent className="p-6">
                  <TrendingUp className="w-10 h-10 text-blue-600 mb-4" />
                  <div className="text-3xl font-bold text-slate-900 mb-2">85%</div>
                  <p className="text-slate-600">Faster expense processing</p>
                </CardContent>
              </Card>
              <Card className="bg-gradient-to-br from-green-50 to-emerald-50 border-green-200 mt-8">
                <CardContent className="p-6">
                  <DollarSign className="w-10 h-10 text-green-600 mb-4" />
                  <div className="text-3xl font-bold text-slate-900 mb-2">$50K+</div>
                  <p className="text-slate-600">Average annual savings</p>
                </CardContent>
              </Card>
              <Card className="bg-gradient-to-br from-purple-50 to-pink-50 border-purple-200">
                <CardContent className="p-6">
                  <Users className="w-10 h-10 text-purple-600 mb-4" />
                  <div className="text-3xl font-bold text-slate-900 mb-2">10K+</div>
                  <p className="text-slate-600">Companies trust us</p>
                </CardContent>
              </Card>
              <Card className="bg-gradient-to-br from-orange-50 to-red-50 border-orange-200 mt-8">
                <CardContent className="p-6">
                  <Shield className="w-10 h-10 text-orange-600 mb-4" />
                  <div className="text-3xl font-bold text-slate-900 mb-2">99.9%</div>
                  <p className="text-slate-600">Fraud detection accuracy</p>
                </CardContent>
              </Card>
            </div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 bg-gradient-to-r from-blue-600 to-indigo-600">
        <div className="container mx-auto px-4 text-center">
          <h2 className="text-4xl font-bold text-white mb-6">
            Ready to transform your expense management?
          </h2>
          <p className="text-xl text-blue-100 mb-8 max-w-2xl mx-auto">
            Join thousands of companies using SpendSense AI to save time and money
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center">
            <Link href="/signup">
              <Button size="lg" className="bg-white text-blue-600 hover:bg-blue-50 text-lg px-8">
                Start Free Trial
                <ArrowRight className="ml-2 w-5 h-5" />
              </Button>
            </Link>
            <Button size="lg" variant="outline" className="border-white text-white hover:bg-white/10 text-lg px-8">
              Schedule Demo
            </Button>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-slate-900 text-slate-300 py-12">
        <div className="container mx-auto px-4">
          <div className="grid md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center space-x-2 mb-4">
                <div className="w-8 h-8 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-lg flex items-center justify-center">
                  <Sparkles className="w-5 h-5 text-white" />
                </div>
                <span className="text-xl font-bold text-white">SpendSense AI</span>
              </div>
              <p className="text-sm">
                AI-powered expense management for modern businesses
              </p>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">Product</h4>
              <ul className="space-y-2 text-sm">
                <li><a href="#" className="hover:text-white">Features</a></li>
                <li><a href="#" className="hover:text-white">Pricing</a></li>
                <li><a href="#" className="hover:text-white">Security</a></li>
                <li><a href="#" className="hover:text-white">Integrations</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">Company</h4>
              <ul className="space-y-2 text-sm">
                <li><a href="#" className="hover:text-white">About</a></li>
                <li><a href="#" className="hover:text-white">Blog</a></li>
                <li><a href="#" className="hover:text-white">Careers</a></li>
                <li><a href="#" className="hover:text-white">Contact</a></li>
              </ul>
            </div>
            <div>
              <h4 className="font-semibold text-white mb-4">Legal</h4>
              <ul className="space-y-2 text-sm">
                <li><a href="#" className="hover:text-white">Privacy</a></li>
                <li><a href="#" className="hover:text-white">Terms</a></li>
                <li><a href="#" className="hover:text-white">Security</a></li>
              </ul>
            </div>
          </div>
          <div className="border-t border-slate-800 mt-8 pt-8 text-center text-sm">
            <p>&copy; 2025 SpendSense AI. All rights reserved.</p>
          </div>
        </div>
      </footer>
    </div>
  );
}
