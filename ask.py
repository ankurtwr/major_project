from fastapi import FastAPI
from pydantic import BaseModel
from policy_rag.test_loop_answers import get_answer

app = FastAPI()

class QueryRequest(BaseModel):
    query:str

@app.post('/ask')
def ask_question(request: QueryRequest):
    answer = get_answer(request.query)
    return {"answer":answer}
    