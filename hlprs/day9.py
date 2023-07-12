class Rope:

    ways = {
        "R": 1,
        "L": -1,
        "U": 1,
        "D": -1
    }

    dirs = {
        "R": 0,
        "L": 0,
        "U": 1,
        "D": 1
    }

    def __init__(self, h: list[int], t: list[int]):
        self.h = h
        self.t = t
        self.vstd = [tuple(t)]

    def move(self, way: str, amnt: int) -> None:
        self.update_h()
        return

    def update_h(self, way: str, amnt: int) -> None:
        drctn = Rope.ways[way]
        idx = Rope.dirs[way]
        self.h[idx] += drctn*amnt
