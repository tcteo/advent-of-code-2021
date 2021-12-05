import re
from collections import namedtuple
import numpy as np

def main():
  vent_coords = parse_vent_coords('input.txt')
  # print(vent_coords)

  grid = coords_to_map(vent_coords)

  # print(f'{np.sum(grid)=}')

  grid_min2 = grid>=2
  print(f'{np.sum(grid_min2)=}')





line_re = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')

Coord = namedtuple('Coord', ['x','y'])

def parse_vent_coords(input_filename):
  vent_coords = []
  with open(input_filename, 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    for l in lines:
      if l=='': continue
      m = line_re.match(l)
      if not m: 
        raise Exception(f'no match on line: {l}')
      
      c1 = Coord(int(m.group(1)),int(m.group(2)))
      c2 = Coord(int(m.group(3)),int(m.group(4)))
      # print(f'{c1} --> {c2}')
      vent_coords.append((c1, c2))
  return vent_coords

def a_lt_b(a, b):
  if a<=b:
    return (a,b)
  else:
    return (b,a)

def coords_to_map(vent_coords):
  # determine map size
  max_x = max([c[0].x for c in vent_coords] + [c[1].x for c in vent_coords])+1
  # print(f'{max_x=}')
  max_y = max([c[0].y for c in vent_coords] + [c[1].y for c in vent_coords])+1
  # print(f'{max_y=}')
  grid = np.zeros((max_x, max_y), dtype=np.int32)
  
  for c in vent_coords:
    if c[0].x == c[1].x:
      # x-line
      a = c[0].y
      b = c[1].y
      a,b = a_lt_b(a,b)
      grid[c[0].x, a:b+1] += 1
    elif c[0].y == c[1].y:
      # y-line
      a = c[0].x
      b = c[1].x
      a,b = a_lt_b(a,b)
      grid[a:b+1, c[0].y] += 1
    elif abs(c[0].x-c[1].x) == abs(c[0].y-c[1].y):
      linelen = abs(c[0].x-c[1].x)
      step = (c[1].x-c[0].x, c[1].y-c[0].y)
      step = (int(step[0]/abs(step[0])), int(step[1]/abs(step[1])))
      # step is one of (1,1), (1,-1), (-1,1), (-1,-1)
      if step not in [(1,1), (1,-1), (-1,1), (-1,-1)]:
        raise Exception(f'cant handle {step=} between {c[0]} and {c[1]}')
      pos = c[0]
      for _ in range(0,linelen+1):
        grid[pos.x, pos.y] += 1
        pos = Coord(pos.x+step[0], pos.y+step[1])

    else:
      raise Exception(f'unhandled line direction between {c[0]} and {c[1]}')

  return grid



if __name__ == '__main__':
  main()

