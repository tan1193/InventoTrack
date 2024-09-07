import os
from fastapi import FastAPI, HTTPException
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.get("/")

def read_root():
    return {"Hello": "World"}

@app.get("/health")
def health_check():
    try:
        # Attempt to fetch data from a table named 'test_table'
        response = supabase.table("products").select("*").execute()
        return response.data
        # log the response
        return {"status": "success", "message": "Successfully connected to Supabase"}
  
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=4820)