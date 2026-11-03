from fastapi import APIRouter
from .. import schema
from ..policy_rag.test_loop_answers import get_answer
from fastapi.responses import FileResponse

router = APIRouter()


@router.post('/ask')
def ask_question(request: schema.QueryRequest):
    answer = get_answer(request.query)
    return {"answer":answer}
    
@router.get('/ask')
def home():
    return FileResponse('templates/index.html')
    