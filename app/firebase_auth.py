import firebase_admin
from firebase_admin import credentials, auth
from fastapi import Request, HTTPException, status, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User

if not firebase_admin._apps:
  cred = credentials.Certificate("service_account.json")
  firebase_admin.initialize_app(cred)

def verify_token_and_register(request: Request, db: Session = Depends(get_db)):
  auth_header = request.headers.get("Authorization")
  if not auth_header or not auth_header.startswith("Bearer "):
    raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")

  token = auth_header.split("Bearer ")[-1]
  try:
      decoded_token = auth.verify_id_token(token)
      uid = decoded_token["uid"]
      
      user = db.query(User).filter(User.firebase_uid == uid).first()
      if user: 
        return user
      
      role = decoded_token.get("role", "customer")
      
      user = User(
        firebase_uid=uid,
        name=decoded_token.get("name") or decoded_token.get("displayName"),
        email=decoded_token.get("email"),
        phone=decoded_token.get("phone_number"),
        role=role
      )
      db.add(user)
      db.commit()
      db.refresh(user)        
      return user
    
  except Exception as e:
    raise HTTPException(status_code=401, detail=f"Invalid Firebase token: {str(e)}")
  
def verify_token_and_login(request: Request, db: Session = Depends(get_db)):
  auth_header = request.headers.get("Authorization")
  if not auth_header or not auth_header.startswith("Bearer "):
    raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")

  token = auth_header.split("Bearer ")[-1]
  try:
      decoded_token = auth.verify_id_token(token)
      uid = decoded_token["uid"]
      
      user = db.query(User).filter(User.firebase_uid == uid).first()
      if not user:
        raise HTTPException(status_code=404, detail="User not registered")
        
      return user
  except Exception as e:
    raise HTTPException(status_code=401, detail=f"Invalid Firebase token: {str(e)}")