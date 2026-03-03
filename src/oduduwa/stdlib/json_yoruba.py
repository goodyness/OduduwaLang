import json

def yipada_si_oro(data):
    """Convert a dictionary or list to JSON string (dumps)."""
    return json.dumps(data)

def yipada_si_nkan(oro):
    """Convert a JSON string back to dictionary or list (loads)."""
    try:
        return json.loads(oro)
    except Exception as e:
        raise Exception(f"Asise kika JSON (JSON Parsing Error): {str(e)}")
