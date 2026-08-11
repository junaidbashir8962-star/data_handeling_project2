import streamlit as st
from pymongo import MongoClient
import certifi

st.title("MongoDB Atlas Connection Test 🚀")

try:
    mongo_uri = st.secrets["MONGO_URI"]
    
    # Pass certifi's CA bundle to tlsCAFile
    client = MongoClient(
        mongo_uri, 
        tlsCAFile=certifi.where(),
        serverSelectionTimeoutMS=5000
    )
    
    # Test connection
    client.admin.command('ping')
    st.success("Successfully connected to MongoDB Atlas! 🎉")
    
    db = client["archive_database"]
    st.write("Database Ready!")

except Exception as e:
    st.error(f"Connection Error: {e}")