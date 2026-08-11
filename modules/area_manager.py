import json
import os

def load_area_config(file_path="config/trade_areas.json"):
    """Reads the JSON area configuration file."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def get_flat_active_areas(config_data):
    """Flattens active trade areas into a clean, sorted list."""
    trade_info = config_data.get("active_trade_areas", {})
    flat_list = set(trade_info.get("standalone_areas", []))
    
    for zone, blocks in trade_info.get("grouped_zones", {}).items():
        for block in blocks:
            flat_list.add(f"{zone} - {block}")
            
    return sorted(list(flat_list))