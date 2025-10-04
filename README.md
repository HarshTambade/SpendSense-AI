## Team Name - Rogers 
## Team Members - Harsh Tambade, Suchita Nigam, Darsh Kalathiya, BharatKumar Gangoman
## Problem statement - Expense Management
# SpendSense AI - Intelligent Expense Management Platform

![SpendSense AI](https://img.shields.io/badge/SpendSense-AI%20Powered-blue)
![Status](https://img.shields.io/badge/Status-Live-success)
![License](https://img.shields.io/badge/License-MIT-green)

## 🚀 Live Demo

[![Watch the video](https://img.youtube.com/vi/d-wj2NMVU20/hqdefault.jpg)](https://youtu.be/d-wj2NMVU20)

## 🔐 Demo Login Credentials

Test the application with these pre-configured accounts:

### 🔴 Admin Account
- **Email**: `admin@spendsense.com`
- **Password**: `Admin@123`
- **Access**: Full system access, company analytics, user management, AI insights

### 🟡 Manager Account
- **Email**: `manager@spendsense.com`
- **Password**: `Manager@123`
- **Access**: Team expense approvals, AI risk analysis, department analytics

### 🟢 Employee Account
- **Email**: `employee@spendsense.com`
- **Password**: `Employee@123`
- **Access**: Submit expenses, upload receipts, track approval status

---

## 📋 Overview

SpendSense AI is a comprehensive expense management platform that leverages artificial intelligence to streamline expense tracking, automate approvals, detect fraud, and provide real-time insights into company spending patterns.

## ✨ Key Features

### 🤖 AI-Powered Intelligence
- **Smart Risk Scoring**: Automatic fraud detection with ML-based risk analysis
- **OCR Receipt Scanning**: Extract data from receipts using advanced OCR
- **Spending Insights**: AI-generated recommendations and pattern analysis
- **Policy Suggestions**: Intelligent expense policy recommendations

### 💼 Expense Management
- **Multi-level Approvals**: Configurable approval workflows
- **Real-time Tracking**: Live expense status updates
- **Receipt Management**: Upload and store receipt images
- **Expense Categories**: Organized expense categorization

### 📊 Analytics & Reporting
- **Interactive Dashboards**: Role-based analytics views
- **Spending Trends**: Visual spending pattern analysis
- **Custom Reports**: Generate detailed expense reports
- **Export Capabilities**: Download reports in multiple formats

### 🌍 Global Support
- **Multi-Currency**: Automatic currency conversion
- **Real-time Exchange Rates**: Live currency rate updates
- **Country-specific Policies**: Localized expense policies

### 🔒 Security & Compliance
- **JWT Authentication**: Secure token-based authentication
- **Role-based Access Control**: Admin, Manager, Employee roles
- **Password Encryption**: Bcrypt password hashing
- **Audit Trails**: Complete expense history tracking

## 🏗️ Technical Architecture

### Backend (FastAPI + PostgreSQL)
```
backend/
├── app/
│   ├── core/           # Security, config
│   ├── models/         # SQLAlchemy models
│   ├── routers/        # API endpoints
│   ├── schemas/        # Pydantic schemas
│   ├── services/       # Business logic
│   └── main.py         # FastAPI application
```

**Tech Stack:**
- FastAPI 0.104.1
- PostgreSQL (SQLAlchemy ORM)
- JWT Authentication
- Bcrypt password hashing
- Hugging Face API integration
- External APIs (Exchange rates, Countries)

### Frontend (Next.js 14 + TypeScript)
```
frontend/
├── app/
│   ├── dashboard/      # Role-based dashboards
│   ├── login/          # Authentication pages
│   ├── signup/
│   └── page.tsx        # Landing page
├── components/         # Reusable UI components
├── contexts/           # React contexts
└── hooks/              # Custom React hooks
```

**Tech Stack:**
- Next.js 14 (App Router)
- TypeScript
- Tailwind CSS
- shadcn/ui components
- Lucide React icons
- Motion animations

## 🎨 UI Features

### Professional Landing Page
- Modern hero section with gradient design
- Interactive dashboard preview
- Feature showcase with icons
- Statistics and benefits section
- Call-to-action sections
- Professional footer

### Enhanced Authentication
- Split-screen design
- Glassmorphism effects
- Animated backgrounds
- Icon-enhanced inputs
- Password visibility toggle
- Remember me functionality

### Role-based Dashboards
- **Admin Dashboard**: Company analytics, user management, AI insights
- **Manager Dashboard**: Team approvals, risk analysis, department stats
- **Employee Dashboard**: Expense submission, history, status tracking

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Node.js 18+
- PostgreSQL
- Bun (optional, for faster package management)

### Backend Setup

1. **Create Database**
```bash
createdb -h localhost spendsense_db
```

2. **Install Dependencies**
```bash
cd backend
pip install -r requirements.txt
```

3. **Configure Environment**
```bash
# Set database connection
export DATABASE_URL="postgresql://user:password@localhost:5432/spendsense_db"
export SECRET_KEY="your-secret-key"
export HUGGINGFACE_API_KEY="your-hf-api-key"
```

4. **Run Backend**
```bash
cd backend
python3 -m uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Frontend Setup

1. **Install Dependencies**
```bash
cd frontend
npm install
# or
bun install
```

2. **Configure Environment**
```bash
# Create .env.local
NEXT_PUBLIC_API_URL=http://localhost:8000
```

3. **Run Frontend**
```bash
npm run dev
# or
bun dev
```

4. **Access Application**
```
http://localhost:3000
```

## 📚 API Documentation

### Authentication Endpoints
- `POST /auth/signup` - Create new user account
- `POST /auth/login` - User login
- `GET /auth/me` - Get current user

### Expense Endpoints
- `POST /expenses/` - Create expense
- `GET /expenses/` - List expenses
- `GET /expenses/{id}` - Get expense details
- `PUT /expenses/{id}` - Update expense
- `DELETE /expenses/{id}` - Delete expense

### Approval Endpoints
- `POST /approvals/` - Create approval
- `GET /approvals/pending` - Get pending approvals
- `PUT /approvals/{id}/approve` - Approve expense
- `PUT /approvals/{id}/reject` - Reject expense

### Analytics Endpoints
- `GET /analytics/company` - Company analytics
- `GET /analytics/user/{id}` - User analytics
- `GET /analytics/trends` - Spending trends

## 🔧 Configuration

### Database Models
- **User**: User accounts with roles
- **Company**: Company information
- **Expense**: Expense records
- **Approval**: Approval workflow
- **RiskScore**: AI risk analysis

### User Roles
- **Admin**: Full system access
- **Manager**: Team management and approvals
- **Employee**: Basic expense submission

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- FastAPI for the excellent web framework
- Next.js for the powerful React framework
- shadcn/ui for beautiful UI components
- Hugging Face for AI/ML capabilities
- PostgreSQL for reliable data storage

## 📞 Support

For support, email support@spendsense.ai or open an issue in the GitHub repository.

## 🗺️ Roadmap

- [ ] Mobile app (React Native)
- [ ] Advanced AI insights
- [ ] Integration with accounting software
- [ ] Multi-language support
- [ ] Advanced reporting features
- [ ] Expense forecasting
- [ ] Budget management
- [ ] Team collaboration features

---

**Built with ❤️ by the SpendSense AI Team**

**Last Updated**: October 4, 2025
