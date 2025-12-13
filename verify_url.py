import httpx

def verify_url_feature():
    base_url = "http://localhost:8000"
    
    # Test 1: Regular ID
    print("Testing ID: 'openai'")
    r = httpx.get(f"{base_url}/api/v1/insight/openai")
    print(f"ID Input -> Status: {r.status_code}, Name: {r.json().get('name')}")
    
    # Test 2: Full URL (passed as path, requires :path support)
    # Note: Client normally needs to encode slashes or use the :path feature. 
    # With {page_id:path}, FastAPI allows slashes.
    target_url = "https://www.linkedin.com/company/google"
    print(f"Testing URL: '{target_url}'")
    r2 = httpx.get(f"{base_url}/api/v1/insight/{target_url}")
    print(f"URL Input -> Status: {r2.status_code}, Name: {r2.json().get('name')}")

if __name__ == "__main__":
    verify_url_feature()
