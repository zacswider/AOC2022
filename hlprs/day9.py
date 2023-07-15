class Rope:

    ways = {
        "R": 1,
        "L": -1,
        "U": 1,
        "D": -1
    }

    dirs = {
        "R": 1,
        "L": 1,
        "U": 0,
        "D": 0
    }

    def __init__(self, h: list[int], t: list[int]):
        self.h = h
        self.t = t
        self.vstd = {tuple(t)}

    def move(self, way: str, amnt: int) -> None:
        self.update_h(way, amnt)
        print("-------------")
        print(f"h: {self.h}")
        print(f"t: {self.t}")
        print(f"goodnuff: {self.goodnuff}")
        print(f"rowdelta: {self.rowdelta}")
        print(f"coldelta: {self.coldelta}")
        print(f"staggered: {self.staggered}")
        if not self.goodnuff:
            print("moving t")
            self.update_t()
        self.vstd.add(tuple(self.t))
        print(f"h: {self.h}")
        print(f"t: {self.t}")
        print(f"goodnuff: {self.goodnuff}")
        print("-------------")
        return

    def update_h(self, way: str, amnt: int) -> None:
        drctn = Rope.ways[way]
        idx = Rope.dirs[way]
        self.h[idx] += drctn*amnt

    def update_t(self) -> None:
        r = self.rowdelta
        c = self.coldelta
        cabs = abs(c)
        rabs = abs(r)
        ctype = int(c / cabs) if cabs != 0 else 0
        rtype = int(r / rabs) if rabs != 0 else 0

        if self.staggered:  # assumed not goodnuff
            self.movet(ctype, rtype)
            cabs -= 1
            rabs -= 1

        if self.staggered:
            raise ValueError("still staggered?!?!")

        if cabs > rabs:
            for _ in range(cabs - 1):
                self.movet(ctype, 0)

        elif rabs > cabs:
            for _ in range(rabs - 1):
                self.movet(0, rtype)

        else:
            raise ValueError("unexpected!")

        if not self.goodnuff:
            raise ValueError("more required")

    def movet(self, col, row) -> None:
        self.t[0] += col
        self.t[1] += row
        self.vstd.add(tuple(self.t))

    @property
    def coldelta(self) -> int:
        return self.h[0] - self.t[0]

    @property
    def rowdelta(self) -> int:
        return self.h[1] - self.t[1]

    @property
    def goodnuff(self) -> bool:
        return all(
            [
                abs(self.coldelta) <= 1,
                abs(self.rowdelta) <= 1
            ]
        )

    @property
    def staggered(self) -> bool:
        return not any(
            [
                self.coldelta == 0,
                self.rowdelta == 0
            ]
        )
