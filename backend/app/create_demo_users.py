from sqlalchemy.orm import Session
from database import SessionLocal
from models.user import User
from models.company import Company
from core.security import get_password_hash

def create_demo_users():
    db = SessionLocal()
    
    try:
        # Check if demo company exists, create if not
        demo_company = db.query(Company).filter(Company.name == "SpendSense Demo").first()
        if not demo_company:
            demo_company = Company(
                name="SpendSense Demo",
                country="United States",
                currency="USD"
            )
            db.add(demo_company)
            db.commit()
            db.refresh(demo_company)
            print(f"✅ Created demo company: {demo_company.name} (ID: {demo_company.id})")
        else:
            print(f"✅ Demo company already exists: {demo_company.name} (ID: {demo_company.id})")
        
        # Demo users data
        demo_users = [
            {
                "email": "admin@spendsense.com",
                "password": "Admin@123",
                "full_name": "Admin User",
                "role": "admin"
            },
            {
                "email": "manager@spendsense.com",
                "password": "Manager@123",
                "full_name": "Manager User",
                "role": "manager"
            },
            {
                "email": "employee@spendsense.com",
                "password": "Employee@123",
                "full_name": "Employee User",
                "role": "employee"
            }
        ]
        
        for user_data in demo_users:
            # Check if user already exists
            existing_user = db.query(User).filter(User.email == user_data["email"]).first()
            
            if existing_user:
                print(f"⚠️  User already exists: {user_data['email']} ({user_data['role']})")
                continue
            
            # Create new user
            hashed_password = get_password_hash(user_data["password"])
            
            new_user = User(
                email=user_data["email"],
                hashed_password=hashed_password,
                full_name=user_data["full_name"],
                role=user_data["role"],
                company_id=demo_company.id
            )
            
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            
            print(f"✅ Created user: {new_user.email} ({new_user.role}) - ID: {new_user.id}")
        
        print("\n" + "="*60)
        print("🎉 Demo users created successfully!")
        print("="*60)
        print("\n📋 Login Credentials:\n")
        print("🔴 Admin:")
        print("   Email: admin@spendsense.com")
        print("   Password: Admin@123\n")
        print("🟡 Manager:")
        print("   Email: manager@spendsense.com")
        print("   Password: Manager@123\n")
        print("🟢 Employee:")
        print("   Email: employee@spendsense.com")
        print("   Password: Employee@123\n")
        print("="*60)
        
    except Exception as e:
        print(f"❌ Error creating demo users: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    create_demo_users()
