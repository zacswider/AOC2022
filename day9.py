from pathlib import Path

from hlprs.day9 import Head, Tail
# from hlprs.day9 import Mid

p = Path("assets/day9test.txt")
print(f"asset founnd: {p.exists()}")

with open(p, "r") as f:
    txt = [line.rstrip() for line in f]

head = Head()
tails = [Tail(parent=head, end=True)]
print(f"Head pos is {head.pos}")

for move in txt:
    way, amnt = move.split(" ")
    print(way, amnt)
    head.move(way=way, amnt=int(amnt))
    print(f"Head pos is {head.pos}")
    for tail in tails:
        tail.chase()
