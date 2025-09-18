from fastapi import APIRouter

router = APIRouter()

@router.get('/farms/{farm_id}')
def get_farm(farm_id: str):
    return {'farm_id': farm_id, 'name': 'Demo Farm'}
