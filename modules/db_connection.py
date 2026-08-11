import streamlit as st
from pymongo import MongoClient
import certifi

@st.cache_resource
def get_database():
    """Initializes and returns cached MongoDB client connection."""
    try:
        mongo_uri = st.secrets["MONGO_URI"]
        client = MongoClient(
            mongo_uri,
            tlsCAFile=certifi.where(),
            serverSelectionTimeoutMS=5000
        )
        # Test connection ping
        client.admin.command('ping')
        return client["main_data_store"]
    except Exception as e:
        st.error(f"MongoDB Connection Error: {e}")
        return None