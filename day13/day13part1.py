import numpy as np
import re

def main():
  grid, foldspec = parse_input('input.txt')
  # grid, foldspec = parse_input('test.txt')
  print(grid.shape)
  print(foldspec)

  for fs in foldspec:
    needs_transpose = False
    if fs[0]!=0: # fold along x=?, vertical
      fold_along = fs[0]
    elif fs[1]!=0: # fold along y=?, horizontal
      fold_along = fs[1]
      needs_transpose = True
    else:
      raise Exception('bad fold')

    print(f'{fold_along=}, {needs_transpose=}')
    if needs_transpose:
      grid = np.transpose(grid)

    # treat as a vertical fold   
    grid_left = grid[0:fold_along, :]
    grid_right = grid[fold_along:, :]
    grid_right = np.flip(grid_right, axis=0)
    pad_to = max(grid_left.shape[0], grid_right.shape[0])
    pad_left = np.zeros((pad_to - grid_left.shape[0], grid_left.shape[1]), dtype=np.bool)
    grid_left = np.concatenate([grid_left, pad_left], axis=0)
    pad_right = np.zeros((pad_to - grid_right.shape[0], grid_right.shape[1]), dtype=np.bool)
    grid_right = np.concatenate([pad_right, grid_right], axis=0)
    if not grid_left.shape == grid_right.shape:
      raise Exception(f'{grid_left.shape=}, {grid_right.shape=}')
    grid = np.logical_or(grid_left, grid_right)

    if needs_transpose:
      grid = np.transpose(grid)
    break # stop at 1

  print(show_grid(grid))

  print(np.sum(grid))

def show_grid(grid):
  s = ''
  for i in range(grid.shape[1]):
    for j in range(grid.shape[0]):
      if grid[j,i]:
        s += '#'
      else:
        s += '.'
    s += '\n'
  return s

re_fold = re.compile(r'^fold along (.)=(\d+)$')

def parse_input(infile):
  with open(infile, 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    blank_line_num = lines.index('')
    print(f'{blank_line_num=}')
    coords = [l.split(',') for l in lines[:blank_line_num]]
    coords = [[int(x), int(y)] for x,y in coords]
    max_x = max([c[0] for c in coords])
    max_y = max([c[1] for c in coords])
    print(f'{max_x=}, {max_y=}')
    grid = np.zeros((max_x+1, max_y+1), dtype=np.bool)
    for cx, cy in coords:
      grid[cx, cy] = True
    
    foldspec = []
    for line in lines[blank_line_num+1:]:
      m = re_fold.match(line)
      if not m:
        raise Exception(f'malformed fold line: {line}')
      value = int(m.group(2))
      if m.group(1)=='x':
        foldspec.append((value,0))
      elif m.group(1)=='y':
        foldspec.append((0,value))
      else:
        raise Exception(f'malformed fold line: {line}')
    return grid, foldspec

if __name__ == '__main__':
  main()