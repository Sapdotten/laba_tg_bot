from asyncio import Lock

lock = Lock()

class LabState:
    _state: bool = False
    _states_name = {
        True: "ОТКРЫТО",
        False: "ЗАКРЫТО"
    }
        
        
    @classmethod
    async def get_status_str(cls) -> str:
        return f"Лаборатория в состоянии {cls._states_name[cls._state]}"
    
    @classmethod
    async def get_status(cls) -> bool:
        return cls._state
    
    @classmethod
    async def change_status(cls, new_state = None) -> bool:
        async with lock:
            if new_state is None:
                cls._state = not cls._state
                return cls._state
            else:
                cls._state = new_state
                return cls._state