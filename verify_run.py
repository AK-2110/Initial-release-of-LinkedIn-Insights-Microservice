import subprocess
import time
import httpx
import sys
import os

def run_verification():
    print("Starting server...")
    # Start uvicorn as a subprocess
    proc = subprocess.Popen(
        [sys.executable, "-m", "uvicorn", "app.main:app", "--port", "8001"],
        cwd=os.getcwd(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    try:
        # Wait for server to start
        print("Waiting for server to be ready...")
        time.sleep(5)
        
        # Make a request
        print("Making request to /api/v1/insight/verify-company")
        response = httpx.get("http://localhost:8001/api/v1/insight/verify-company", timeout=10)
        
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
        
        if response.status_code == 200:
            print("SUCCESS: verification passed!")
        else:
            print("FAILURE: Validation failed.")
            print(proc.stderr.read().decode())
            
    except Exception as e:
        print(f"Error during verification: {e}")
        # Print server output
        logs = proc.stderr.read().decode()
        print(f"Server Logs:\n{logs}")
    finally:
        print("Stopping server...")
        proc.terminate()
        proc.wait()

if __name__ == "__main__":
    run_verification()
