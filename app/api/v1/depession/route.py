from fastapi import APIRouter
from .service import get_depression
from .schema import DepressionRequest

router = APIRouter()

@router.post('/depession', tags=['Depression'])
def assess_depression(data: DepressionRequest):
    return get_depression()

@router.get('/info', tags=['Depression'])
def info():
    return {"service": "This endpoint provides depression assessment services."}

@router.delete('/depression', tags=['Depression'])
def delete_depression_record(record_id: int):
    return {"status" : "deleted", "record_id": record_id}

@router.put('/depression', tags=['Depression'])
def update_depression_record(record_id: int, data: DepressionUpdate):
    return {"status": "updated", "record_id": record_id, "data": data}

@router.patch('/depression', tags=['Depression'])
def patch_depression_record(record_id: int, data: DepressionPatch):
    return {"status": "patched", "record_id": record_id, "data": data}