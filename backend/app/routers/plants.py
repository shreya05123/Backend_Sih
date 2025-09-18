from fastapi import APIRouter

router = APIRouter()

@router.get('/plants/{plant_id}')
def get_plant(plant_id: str):
    return {'plant_id': plant_id, 'species': 'unknown'}
