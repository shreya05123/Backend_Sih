from fastapi import APIRouter

router = APIRouter()

@router.post('/actuators/{actuator_id}/command')
def actuator_cmd(actuator_id: str, command: dict):
    return {'actuator_id': actuator_id, 'command': command, 'status':'sent'}
