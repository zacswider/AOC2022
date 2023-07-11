from pathlib import Path

from hlprs.day8 import getrow, getcol, Tree

p = Path("assets/day8.txt")
print(f"asset found: {p.exists()}")

with open(p, "r") as f:
  txt = [l.rstrip() for l in f]

trees = []
for r in range(len(txt)):
  for c in range(len(txt[0])):
    #print(f"r: {r}")
    #print(f"c: {c}")
    row = getrow(txt, r)
    col = getcol(txt, c)
    val = txt[r][c]
    #print(f"{val} found at idx {c} of row {row}")
    #print(f"{val} found at idx {r} of col {col}")
    tree = Tree(row, c, col, r)
    #print(f"visible: {tree.visible}")
    trees.append(tree)
    if r == 2 and c == 3:
      pass
      #print(Tree(row, c, col, r).score)

vis = [t for t in trees if t.visible]

print(f"visible trees: {len(vis)}")

scores = [t.score for t in trees]

print(f"highest score: {max(scores)}")
