import os
import glob
import sys
import pathlib

def main():
    path = pathlib.Path(sys.argv[1])
    for folder in path.iterdir():
        if folder.is_dir():
            files = sorted(folder.iterdir(), key=os.path.getmtime)  # Sort files by creation time
            counter = 1
            for file in files:
                if file.is_file():
                    x = view(counter)
                    y = DayOrNight(counter)
                    new_file = f"City{folder.name}-View{x}-{y}{file.suffix}"
                    file.rename(path / folder.name / new_file)
                    counter += 1


def view(x):
      if x == 1 or x == 2:
            return "1"
      elif x == 3 or x == 4:
            return "2"
      elif x == 5 or x == 6:
            return "3"
      else:
            return "4"
      
def DayOrNight(x):
      if (x%2) == 0:
            return "Night"
      else:
            return "Day"


if __name__ == "__main__":
    main()