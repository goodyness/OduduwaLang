import urllib.request
import urllib.error

def gba(url):
    """Perform a GET request and return the string response (gba wole)."""
    try:
        with urllib.request.urlopen(url) as response:
            return response.read().decode('utf-8')
    except urllib.error.URLError as e:
        raise Exception(f"Asise Ayelujara (Network Error): {str(e)}")
