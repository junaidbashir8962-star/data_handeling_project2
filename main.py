import streamlit as st
import pandas as pd

from modules.ui import load_css, render_header
from modules.db_connection import get_database
from modules.area_manager import load_area_config, get_flat_active_areas
from modules.data_cleaner import clean_dataframe
from modules.validation import add_record_hashes
from modules.uploader import bulk_upload_to_mongo

# 1. Page Configuration
st.set_page_config(page_title="Data Handling Pipeline", page_icon="⚡", layout="wide")
load_css("assets/styles.css")

# 2. Header
render_header("⚡ Data Ingestion & Area Pipeline", "Automated Processing, Validation, & MongoDB Ingestion")

# 3. Load Configurations & DB Connection
area_config = load_area_config()
active_areas_flat = get_flat_active_areas(area_config)

db = get_database()

if db is not None:
    st.sidebar.success("✅ Connected to MongoDB Atlas")

# 4. Sidebar Area Registry Inspector
st.sidebar.markdown("---")
st.sidebar.subheader("📍 Trade Network Registry")

if st.sidebar.button("👁️ View Active Trade Areas"):
    st.subheader("🗺️ Active Trade Areas Registry")
    st.dataframe(pd.DataFrame(active_areas_flat, columns=["Area / Zone Name"]), use_container_width=True)

# 5. Main Processing Flow
st.markdown("### 📁 Upload File for Ingestion")
uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file and db is not None:
    try:
        # Load Raw Data
        df_raw = pd.read_csv(uploaded_file) if uploaded_file.name.endswith(".csv") else pd.read_excel(uploaded_file)

        st.subheader("Raw Data Preview")
        st.dataframe(df_raw.head(5), use_container_width=True)

        # Step A: Standardize & Clean
        df_clean = clean_dataframe(df_raw)
        
        # Step B: Deduplication Hash
        df_processed = add_record_hashes(df_clean)

        st.success(f"Processed {len(df_processed)} records successfully!")

        # Step C: Upload Execution
        if st.button("🚀 Push Records to MongoDB", type="primary"):
            with st.spinner("Uploading to MongoDB Atlas..."):
                inserted, updated = bulk_upload_to_mongo(db, "processed_records", df_processed)
            st.success(f"Upload Complete! Inserted: {inserted} new records | Updated: {updated} records.")
            st.balloons()

    except Exception as e:
        st.error(f"Error processing file: {e}")