# 🔐 SpendSense AI - Demo Login Credentials

## Live Application
**URL**: https://real-banks-prove.lindy.site

---

## 📋 Test User Accounts

### 🔴 Admin Account
**Full Access - Company Management**

```
Email: admin@spendsense.com
Password: Admin@123
```

**Access & Features:**
- ✅ Company-wide analytics dashboard
- ✅ User management (add, edit, delete users)
- ✅ AI-generated insights and recommendations
- ✅ Expense policy configuration
- ✅ All expense approvals across company
- ✅ System settings and configuration
- ✅ Export reports and data
- ✅ View all departments and teams

---

### 🟡 Manager Account
**Team Management & Approvals**

```
Email: manager@spendsense.com
Password: Manager@123
```

**Access & Features:**
- ✅ Team expense approval workflow
- ✅ AI risk analysis for expenses
- ✅ Department-level analytics
- ✅ Team member expense tracking
- ✅ Spending pattern analysis
- ✅ Budget monitoring
- ✅ Team reports generation
- ✅ Approval notifications

---

### 🟢 Employee Account
**Basic User - Expense Submission**

```
Email: employee@spendsense.com
Password: Employee@123
```

**Access & Features:**
- ✅ Submit new expenses
- ✅ Upload receipt images (OCR scanning)
- ✅ View personal expense history
- ✅ Track approval status
- ✅ Receive approval/rejection notifications
- ✅ Edit pending expenses
- ✅ View spending summaries
- ✅ Download personal reports

---

## 🚀 Quick Start Guide

### Step 1: Access the Application
Navigate to: https://real-banks-prove.lindy.site

### Step 2: Choose Your Role
Select one of the demo accounts above based on what you want to test

### Step 3: Login
1. Click "Sign In" button
2. Enter the email and password
3. Click "Sign In"

### Step 4: Explore Features
- **Admin**: Check company analytics, manage users, view AI insights
- **Manager**: Review pending approvals, analyze team spending
- **Employee**: Submit an expense, upload a receipt

---

## 🎯 Testing Scenarios

### Scenario 1: Employee Submits Expense
1. Login as **Employee** (`employee@spendsense.com`)
2. Navigate to "Submit Expense"
3. Fill in expense details (amount, category, description)
4. Upload a receipt image
5. Submit for approval

### Scenario 2: Manager Reviews & Approves
1. Login as **Manager** (`manager@spendsense.com`)
2. Go to "Pending Approvals"
3. Review the expense submitted by employee
4. Check AI risk score
5. Approve or reject with comments

### Scenario 3: Admin Views Analytics
1. Login as **Admin** (`admin@spendsense.com`)
2. View company-wide dashboard
3. Check spending trends
4. Review AI-generated insights
5. Manage users and policies

---

## 🔧 Technical Details

### Database Information
- **Database**: PostgreSQL (spendsense_db)
- **Company**: SpendSense Demo
- **Currency**: USD
- **Country**: United States

### User Roles Hierarchy
```
Admin (Full Access)
  └── Manager (Team Management)
        └── Employee (Basic User)
```

### API Endpoints
- **Login**: `POST /auth/login`
- **Signup**: `POST /auth/signup`
- **Expenses**: `/expenses/*`
- **Approvals**: `/approvals/*`
- **Analytics**: `/analytics/*`

---

## 📊 Features to Test

### AI-Powered Features
- ✨ Automatic risk scoring for expenses
- 🔍 OCR receipt scanning and data extraction
- 📈 Spending pattern analysis
- 💡 Policy recommendations
- 🚨 Fraud detection alerts

### Workflow Features
- 📝 Multi-level approval workflows
- 🔔 Real-time notifications
- 📊 Interactive dashboards
- 📁 Receipt management
- 💱 Multi-currency support

### Analytics Features
- 📈 Spending trends visualization
- 🏢 Department-wise analytics
- 👥 User-level reports
- 📅 Time-based analysis
- 📊 Custom report generation

---

## 🔒 Security Notes

⚠️ **Important Security Information:**

1. **Demo Purposes Only**: These credentials are for testing and demonstration
2. **Not for Production**: Do not use these accounts for real expense data
3. **Public Access**: These credentials are publicly available
4. **Data Privacy**: Any data entered may be visible to other testers
5. **Regular Resets**: Demo data may be reset periodically

---

## 🐛 Troubleshooting

### Login Issues
- **Problem**: "Invalid email or password"
- **Solution**: Ensure you're using the exact credentials (case-sensitive)
- **Check**: Make sure there are no extra spaces

### Dashboard Not Loading
- **Problem**: Blank dashboard after login
- **Solution**: Refresh the page (F5)
- **Check**: Ensure JavaScript is enabled

### Features Not Working
- **Problem**: Buttons or forms not responding
- **Solution**: Clear browser cache and cookies
- **Check**: Try a different browser (Chrome, Firefox, Safari)

---

## 📞 Support

For issues or questions:
- **GitHub**: https://github.com/HarshTambade/SpendSense-AI
- **Documentation**: See README.md
- **API Docs**: https://itchy-hats-own.lindy.site/docs

---

## 🎨 UI Features

### Professional Design
- ✨ Modern gradient backgrounds
- 🎭 Glassmorphism effects
- 🎬 Smooth animations
- 📱 Responsive design
- 🌙 Professional color scheme

### User Experience
- 🎯 Intuitive navigation
- 🔍 Clear visual hierarchy
- ⚡ Fast loading times
- 📊 Interactive charts
- 🎨 Icon-enhanced inputs

---

**Last Updated**: October 4, 2025  
**Version**: 1.0  
**Status**: ✅ Active & Working

---

**Built with ❤️ by the SpendSense AI Team**
