import pandas as pd

def clean_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    """Cleans null values, standardizes column names, and trims whitespace."""
    # Standardize column headers
    df.columns = [str(col).strip().lower().replace(" ", "_") for col in df.columns]
    
    # Fill NaN / NaT values so PyMongo handles serialization seamlessly
    df = df.fillna("")
    
    # Strip whitespace from string columns
    for col in df.select_dtypes(include=["object", "string"]).columns:
        df[col] = df[col].astype(str).str.strip()
        
    return df