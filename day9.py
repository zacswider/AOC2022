from pathlib import Path

from hlprs.day9 import Rope

p = Path("assets/day9.txt")
print(f"asset founnd: {p.exists()}")

with open(p, "r") as f:
    txt = [line.rstrip() for line in f]

rope = Rope(h=[0, 0], t=[0, 0])
print(f"num tail positions: {len(rope.vstd)}")

for move in txt:
    way, amnt = move.split(" ")
    print(way, amnt)
    rope.move(way=way, amnt=int(amnt))

print(f"locs visited: {len(rope.vstd)}")
