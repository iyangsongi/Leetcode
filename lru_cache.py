class LRUCache:
    def __init__(self, capacity: int):
        self.cap=capacity
        self.dict={}
        self.frq=[]
        
    def get(self, key: int) -> int:
        if key in self.dict:
            self.frq.remove(key)
            self.frq.append(key)
        return self.dict.get(key,-1)         

    def put(self, key: int, value: int) -> None:
        if key not in self.dict:
            if len(self.dict)+1>self.cap:
                self.dict.pop(self.frq.pop(0))
        else:
            self.frq.remove(key)
        self.frq.append(key)
        self.dict[key]=value