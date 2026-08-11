import hashlib
import pandas as pd

def add_record_hashes(df: pd.DataFrame) -> pd.DataFrame:
    """Generates unique MD5 hash ID for each row to handle deduplication."""
    def generate_hash(row):
        row_str = "".join(str(val) for val in row.values)
        return hashlib.md5(row_str.encode('utf-8')).hexdigest()

    df['record_hash'] = df.apply(generate_hash, axis=1)
    return df