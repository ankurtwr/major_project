from fastapi import FastAPI
from pydantic import BaseModel
from policy_rag.test_loop_answers import get_answer
from fastapi.responses import FileResponse

app = FastAPI()

class QueryRequest(BaseModel):
    query:str

@app.post('/ask')
def ask_question(request: QueryRequest):
    answer = get_answer(request.query)
    return {"answer":answer}
    
@app.get('/')
def home():
    return FileResponse('templates/index.html')
    