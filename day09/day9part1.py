import numpy as np

def main():
  grid = parse_input('input.txt')
  print(f'{grid=}')
  mingrid = min_points(grid)
  print(f'{mingrid=}')

  min_values = grid[mingrid]
  risk_sum = np.sum(min_values+1)
  # 329 is too low
  print(f'{risk_sum=}')


def parse_input(infile):
  with open(infile, 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    digits = [[int(x) for x in list(l)] for l in lines]
    return np.array(digits, dtype=np.int8)

def min_points(grid):
  mingrid = np.zeros(grid.shape, dtype=np.bool)
  imax = grid.shape[0]
  jmax = grid.shape[1]
  for i in range(0, imax):
    for j in range(0, jmax):
      lt_n = True if i==0      else (grid[i,j] < grid[i-1,j])
      lt_s = True if i==imax-1 else (grid[i,j] < grid[i+1,j])
      lt_w = True if j==0      else (grid[i,j] < grid[i,j-1])
      lt_e = True if j==jmax-1 else (grid[i,j] < grid[i,j+1])
      mingrid[i,j] = lt_n and lt_s and lt_w and lt_e
  return mingrid

if __name__ == '__main__':
  main()