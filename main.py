import streamlit as st
from pymongo import MongoClient

st.set_page_config(page_title="MongoDB Test", page_icon="⚡")

st.title("MongoDB Atlas Connection Test 🚀")

# 1. Fetch connection string securely from secrets
try:
    mongo_uri = st.secrets["MONGO_URI"]
    
    # Initialize PyMongo Client
    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
    
    # Test server response (Ping)
    client.admin.command('ping')
    st.success("Successfully connected to MongoDB Atlas! 🎉")
    
    # Create test Database and Collection
    db = client["archive_database"]
    collection = db["test_collection"]
    
    # Insert a dummy record
    sample_doc = {
        "status": "Success",
        "message": "Database pipeline connection working perfectly!"
    }
    result = collection.insert_one(sample_doc)
    
    st.info(f"Test record inserted with Document ID: `{result.inserted_id}`")

except Exception as e:
    st.error(f"Connection Error: {e}")