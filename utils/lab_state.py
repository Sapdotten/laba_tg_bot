from asyncio import Lock

lock = Lock()

class LabState:
    _state: bool
    _states_name = {
        True: "ОТКРЫТО",
        False: "ЗАКРЫТО"
    }
        
        
    @classmethod
    async def get_status_str(cls) -> str:
        return f"Лаборатория в состояни {cls._states_name[cls._state]}"
    
    @classmethod
    async def get_status(cls):
        return cls._state
    
    @classmethod
    async def change_status(cls, new_state = None) -> str:
        async with lock:
            if new_state is None:
                cls._state = not cls._state
                return
            if cls._state == new_state:
                return f"Лаборатория уже в состоянии {cls._states_name[cls._state]}"
            else:
                cls._state = new_state
                return f"Лаборатория переведена в состяние {cls._states_name[cls._state]}"
        