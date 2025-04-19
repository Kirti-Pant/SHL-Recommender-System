from fastapi import FastAPI
from pydantic import BaseModel
from utils.recommender import recommend_assessments
from utils.query_enhancer import enhance_query

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "👋 Welcome to the SHL Assessment Recommender API. Use POST /recommend or visit /docs."
    }

class QueryInput(BaseModel):
    query: str

@app.post("/recommend")
async def recommend(input_data: QueryInput):
    enhanced_query = enhance_query(input_data.query)
    results = recommend_assessments(enhanced_query)
    return results


