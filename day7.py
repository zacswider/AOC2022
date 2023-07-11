from pathlib import Path

from hlprs.day7 import (
    linetype, Folder, File
)

p = Path("./assets/day7.txt")


def main():
  print("running main")

  with open(p, "r") as f:
    txt = [l.rstrip() for l in f.readlines()]
  
  # starting dir 
  curr = Folder("/", None)
  top = curr

  for idx, l in enumerate(txt[1:]):
    
    lt = linetype(l) 
    
    if lt == "file":
      size, name = l.split(" ")
      print(f"adding {name} of size {size} to {curr.name}")
      curr.files[name] = File(size, name)
    elif lt == "folder":
      _, name = l.split(" ")
      newfolder = Folder(name, curr)
      curr.folders[name] = newfolder
    elif lt == "step up":
      parent = curr.parent
      print(f"moving up {curr.name}->{parent.name}")
      curr = parent
    elif lt == "step down":
      dest = l.split(" ")[-1]
      print(f"moving down {curr.name}->{dest}")
      curr = curr.folders[dest]
    else:
      continue

  
  def adddirs(d: Folder, dlist: list) -> None:
    for folder in d.folders.values():
      dlist.append(folder)
      adddirs(folder, dlist)
  
  alldirs = [top]
  adddirs(top, alldirs)
  
  
  smalldirs = []
  dirsizes = []
  sizes = 0
  for d in alldirs:
    tot = d.total_size
    dirsizes.append(tot)
    print(f"{d.name} = {tot}")
    if tot <= 100000:
      smalldirs.append(d)
      sizes += tot
  print(f"{len(alldirs)}, {len(smalldirs)}")
  print(sizes)

  total = 70000000
  current = top.total_size
  needed = 30000000
  free = total - current
  neededtodelete = needed - free
  print(f"current:{current}")
  print(f"free:{free}")
  print(f"need to delete {neededtodelete}")
  
  ascending = sorted(dirsizes) 
  for idx, s in enumerate(ascending):
    print(s)
    if s > neededtodelete:
      #print(sorted(dirsizes)[idx-1]) 
      break

if __name__ == "__main__":
  main()
