import time
import datetime

def bayi():
    """Return the current time in seconds (asiko bayi)."""
    return time.time()

def asiko_kika():
    """Return a readable datetime string (asiko kika)."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def sun(iseju_aaya):
    """Sleep for X seconds (sun)."""
    time.sleep(iseju_aaya)
