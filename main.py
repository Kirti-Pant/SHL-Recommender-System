from fastapi import FastAPI
from pydantic import BaseModel
from utils.recommender import recommend_assessments
from utils.query_enhancer import enhance_query

app = FastAPI()

class QueryInput(BaseModel):
    query: str

@app.post("/recommend")
async def recommend(input_data: QueryInput):
    enhanced_query = enhance_query(input_data.query)
    results = recommend_assessments(enhanced_query)
    return results

