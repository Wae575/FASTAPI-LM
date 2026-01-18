from fastapi import APIRouter
from .recommend.route import router as recommend_router
from .flight.route import router as flight_router   
from .depession.route import router as depression_router

app_router = APIRouter()

app_router.include_router(
    recommend_router,
    prefix='/recommend',
    tags=['Recommendations']
)

app_router.include_router(
    depression_router,
    prefix='/depression',
    tags=['Depression']
)