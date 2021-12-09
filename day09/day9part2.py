import numpy as np

def main():
  grid = parse_input('input.txt')
  # grid = parse_input('test.txt')
  # print(f'{grid=}')
  mingrid = min_points(grid) # grid with True at minima
  # print(f'{mingrid=}')

  min_locations_where = np.where(mingrid==True) # two arrays, list of i's and list of j's
  min_locations = list(zip(*min_locations_where)) # a list of tuples [(i,j),(i,j),...]
  # print(f'{len(min_locations)=}')
  basin_sizes = []
  for mi,mj in min_locations:
    bs = basin_size(grid, mi, mj)
    basin_sizes.append(bs)
  print(f'{basin_sizes=}')
  print(f'{len(basin_sizes)=}')

  top_three = sorted(basin_sizes, key=lambda x:-x)[0:3]

  size_product = 1
  for s in top_three:
    size_product *= s
  print(f'{size_product=}')
  

def basin_size(grid, mi, mj):
  basin_loc = np.zeros(grid.shape, dtype=np.bool)
  basin_loc[mi,mj]=True # min point is part of the basin
  basin_size = np.sum(basin_loc)
  # print(f'basin starting at {mi},{mj}')
  while True:
    # try to expand the basin
    basin_positions = list(zip(*(np.where(basin_loc==True))))
    for bp in basin_positions:
      for movei, movej in [(0,-1),(0,1),(-1,0),(1,0)]:
        i = bp[0] + movei
        j = bp[1] + movej
        if i<0 or i>=grid.shape[0]: continue # off the grid
        if j<0 or j>=grid.shape[1]: continue # off the grid
        if basin_loc[i,j]==True: continue # already marked
        if grid[i,j]>=9: continue # limit of basin
        basin_loc[i,j] = True # set as part of the current basin
        # print(f'              add {i},{j}')
    new_basin_size = np.sum(basin_loc)
    if new_basin_size == basin_size:
      break # no growth, we are done expanding the basin
    basin_size = new_basin_size
  # print(f'basin_loc:\n{basin_loc}')
  return basin_size

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