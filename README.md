# SpendSense AI - Smart Expense Management Platform

An AI-powered expense management platform with intelligent approvals, OCR receipt processing, and real-time analytics.

## 🚀 Features

### Core Functionality
- **Smart Expense Submission**: Upload receipts with OCR text extraction
- **AI-Powered Risk Analysis**: Automatic fraud detection and risk scoring
- **Multi-Level Approval Workflows**: Sequential approval chains with role-based access
- **Real-Time Analytics**: Interactive dashboards with spending insights
- **Currency Conversion**: Automatic exchange rate conversion for international expenses
- **Policy Suggestions**: AI-generated policy recommendations based on spending patterns

### Role-Based Dashboards
- **Employee Dashboard**: Submit expenses, track status, view history
- **Manager Dashboard**: Review and approve team expenses with AI risk insights
- **Admin Dashboard**: Company-wide analytics, user management, policy oversight

### AI Integrations
- **OCR Processing**: Hugging Face API for receipt text extraction
- **Risk Scoring**: ML-based fraud detection and anomaly detection
- **Category Classification**: Automatic expense categorization
- **Spending Insights**: AI-powered analytics and recommendations

## 🛠️ Tech Stack

### Backend
- **FastAPI**: High-performance Python web framework
- **PostgreSQL**: Relational database with SQLAlchemy ORM
- **JWT Authentication**: Secure token-based authentication
- **Pydantic**: Data validation and serialization
- **Passlib + Bcrypt**: Password hashing

### Frontend
- **Next.js 14**: React framework with App Router
- **TypeScript**: Type-safe development
- **Tailwind CSS**: Utility-first CSS framework
- **shadcn/ui**: Beautiful UI components
- **Recharts**: Data visualization

### External APIs
- **Hugging Face**: OCR and NLP processing
- **Exchange Rate API**: Real-time currency conversion
- **REST Countries API**: Country information

## 📦 Installation

### Prerequisites
- Python 3.10+
- Node.js 18+
- PostgreSQL 14+

### Backend Setup

1. Create PostgreSQL database:
```bash
createdb -h localhost spendsense_db
```

2. Install Python dependencies:
```bash
cd backend
pip install -r requirements.txt
```

3. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Run database migrations:
```bash
python -m alembic upgrade head
```

5. Start the backend server:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### Frontend Setup

1. Install dependencies:
```bash
cd frontend
npm install
```

2. Configure environment:
```bash
cp .env.local.example .env.local
# Edit .env.local with your API URL
```

3. Start the development server:
```bash
npm run dev
```

## 🔑 Environment Variables

### Backend (.env)
```
DATABASE_URL=postgresql://user:password@localhost:5432/spendsense_db
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
HUGGINGFACE_API_KEY=your-huggingface-api-key
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## 📱 Usage

### Creating an Account
1. Navigate to `/signup`
2. Enter company details and admin credentials
3. Complete registration to access the admin dashboard

### Submitting an Expense (Employee)
1. Log in to your employee account
2. Click "Submit Expense" on the dashboard
3. Fill in expense details and upload receipt
4. Submit for approval

### Approving Expenses (Manager/Admin)
1. Navigate to the dashboard
2. Review pending approvals with AI risk scores
3. Approve or reject with comments

### Viewing Analytics (Admin)
1. Access the Admin Dashboard
2. View spending by category, vendor, and time period
3. Review AI-generated insights and policy suggestions

## 🏗️ Project Structure

```
spendsense-ai/
├── backend/
│   ├── app/
│   │   ├── core/          # Security, config
│   │   ├── models/        # Database models
│   │   ├── routers/       # API endpoints
│   │   ├── schemas/       # Pydantic schemas
│   │   └── main.py        # FastAPI app
│   ├── uploads/           # Receipt storage
│   └── requirements.txt
├── frontend/
│   ├── app/               # Next.js pages
│   ├── components/        # React components
│   ├── contexts/          # Auth context
│   └── lib/               # Utilities
└── README.md
```

## 🔒 Security Features

- JWT-based authentication
- Password hashing with bcrypt
- Role-based access control (RBAC)
- CORS protection
- SQL injection prevention via ORM
- Input validation with Pydantic

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License.

## 👥 Authors

- **Harsh Tambade** - [GitHub](https://github.com/HarshTambade)

## 🙏 Acknowledgments

- Hugging Face for OCR API
- shadcn/ui for beautiful components
- FastAPI and Next.js communities

## 📞 Support

For support, email prepaiindia@gmail.com or open an issue on GitHub.
