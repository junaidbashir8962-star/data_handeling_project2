from pymongo import UpdateOne

def bulk_upload_to_mongo(db, collection_name: str, df: pd.DataFrame):
    """Inserts or updates records into MongoDB using upsert on record_hash."""
    collection = db[collection_name]
    records = df.to_dict(orient="records")
    
    operations = [
        UpdateOne(
            {"record_hash": record["record_hash"]},
            {"$set": record},
            upsert=True
        ) for record in records
    ]
    
    if operations:
        result = collection.bulk_write(operations)
        return result.upserted_count, result.modified_count
    return 0, 0