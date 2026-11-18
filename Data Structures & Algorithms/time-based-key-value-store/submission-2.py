import bisect
class TimeMap:
    def __init__(self): # bisect
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = ([], [])
        times, vals = self.store[key]
        times.append(timestamp)
        vals.append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        times, vals = self.store[key]
        idx = bisect.bisect_right(times, timestamp) - 1
        return vals[idx] if idx >= 0 else ""