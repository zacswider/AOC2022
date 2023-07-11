

NUMS = ["1","2","3","4","5","6","7","8","9","0"]


def linetype(line: str) -> str:
  if line.startswith("$"):      # cmd line
    bits = line.split(" ")
    if bits[1] == "ls":
      return "ls"
    if bits[1] == "cd" and bits[-1] == "..":
      return "step up"
    else:
      return "step down"
    return line.split(" ")[1]
  elif line.startswith("dir"):
    return "folder"
  elif line[0] in NUMS:
    return "file"
  else:
    raise ValueError(f"unknown line type: {line}")


class Folder:
  def __init__(self, name, parent):
    self.name = name
    self.parent = parent
    self.files = {}
    self.folders = {}
  
  @property
  def folder_names(self):
    return [i for i in self.folders.keys()]
  
  @property
  def size(self):
    return sum(
      [int(f.size) for f in self.files.values()]
    )
  
  @property
  def total_size(self):
    return sum(
      [int(d.total_size) for d in self.folders.values()]
    ) + self.size


class File:
  def __init__(self, size, name):
    self.name = name
    self.size = size
  
  

    