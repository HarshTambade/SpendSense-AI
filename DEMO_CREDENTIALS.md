# SpendSense AI - Demo Login Credentials

## Test User Accounts

Use these credentials to test different user roles and features in SpendSense AI.

### 🔴 Admin Account
**Role**: Administrator (Full system access)
- **Email**: `admin@spendsense.com`
- **Password**: `Admin@123`
- **Access**: 
  - Company analytics dashboard
  - User management
  - AI insights and policy suggestions
  - All expense approvals
  - System settings

### 🟡 Manager Account
**Role**: Manager (Team management)
- **Email**: `manager@spendsense.com`
- **Password**: `Manager@123`
- **Access**:
  - Team expense approvals
  - AI risk analysis
  - Department analytics
  - Team member expenses

### 🟢 Employee Account
**Role**: Employee (Basic user)
- **Email**: `employee@spendsense.com`
- **Password**: `Employee@123`
- **Access**:
  - Submit expenses
  - Upload receipts
  - View expense history
  - Track approval status

---

## Quick Login Links

- **Live Application**: https://real-banks-prove.lindy.site
- **Login Page**: https://real-banks-prove.lindy.site/login

## Features to Test

### As Admin:
1. View company-wide analytics
2. Manage users and roles
3. Review AI-generated insights
4. Configure expense policies
5. Approve/reject all expenses

### As Manager:
1. Review team expenses
2. Approve/reject submissions
3. View AI risk scores
4. Monitor team spending patterns
5. Generate team reports

### As Employee:
1. Submit new expenses
2. Upload receipt images
3. Track expense status
4. View expense history
5. Receive approval notifications

---

## Database Setup

These accounts are pre-configured in the database with the following structure:

```sql
-- Admin User
INSERT INTO users (email, hashed_password, full_name, role, company_id)
VALUES ('admin@spendsense.com', '<hashed>', 'Admin User', 'admin', 1);

-- Manager User
INSERT INTO users (email, hashed_password, full_name, role, company_id)
VALUES ('manager@spendsense.com', '<hashed>', 'Manager User', 'manager', 1);

-- Employee User
INSERT INTO users (email, hashed_password, full_name, role, company_id)
VALUES ('employee@spendsense.com', '<hashed>', 'Employee User', 'employee', 1);
```

---

## Security Notes

⚠️ **Important**: These are demo credentials for testing purposes only. 
- Do not use these credentials in production
- Change passwords after initial setup
- Implement proper password policies for production use

---

**Last Updated**: October 4, 2025
