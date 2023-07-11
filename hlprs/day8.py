
def getcol(lol, col):
  return [i for i in lol[col]]

def getrow(lol, row):
  newrow = []
  for col in lol:
    newrow.append(col[row])
  return newrow


class Tree:
  def __init__(
    self, 
    row: list[int], 
    rowidx: int, 
    col: list[int], 
    colidx: int) -> None:
    self.row = row
    self.rowidx = rowidx
    self.col = col
    self.colidx = colidx
  
  @property
  def visible(self) -> bool:
    return any(
      [
        self.colisvis(),
        self.rowisvis()
      ]
    )
    
  @property
  def score(self) -> int:
    a = self.calcscore(self.row, self.rowidx, "f")
    b = self.calcscore(self.row, self.rowidx, "r")
    c = self.calcscore(self.col, self.colidx, "f")
    d = self.calcscore(self.col, self.colidx, "r")
    #print(a,b,c,d)
    return a * b * c * d
  
  def isvis(self, l: list, idx: int) -> bool:
    if idx == 0 or idx == len(l) - 1:
      return True
    val = l[idx]
    return all(
      [
        l[i] < val
        for i in range(idx + 1, len(l))
      ]
    ) or all(
      [
        l[i] < val
        for i in range(0, idx)
      ]
    )
  
  def colisvis(self) -> bool:
    return self.isvis(self.col, self.colidx)
  
  def rowisvis(self) -> bool:
    return self.isvis(self.row, self.rowidx)
  
  def calcscore(
    self, 
    l: list, 
    idx: int, 
    way: str) -> int:
    
    val = l[idx]
    if way == "f":
      trees = l[idx+1:]
    else:
      trees = list(reversed(l[0:idx]))
    
    s = 0
    for tree in trees:
      if tree >= val:
        s+=1
        break
      else:
        s+=1
     
    if idx == 0 or idx == len(l) - 1:
      s = 0
    """
    print("---") 
    print(f"l is {l}")
    print(f"idx is {idx}")
    print(f"val is {val}")
    print(f"trees is {trees}")
    print(f"score is {s}")
    """
    return s
    
  
  
  
  
  
  



