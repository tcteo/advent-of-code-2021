import numpy as np
import scipy.signal

def main():
  # grid = parse_input('test.txt')
  grid = parse_input('input.txt')
  # print(grid)

  flash_sum = 0
  for s in range(100):
    grid, flashes = step(grid)
    flash_sum += np.sum(flashes)
  # print(grid)
  print(f'{flash_sum=}')

def parse_input(infile):
  with open(infile, 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    grid = [[int(x) for x in line] for line in lines]
    return np.array(grid, dtype=np.int32)

flash_conv = np.array([[1,1,1],[1,0,1],[1,1,1]])

def step(grid):
  flashed_count = None
  flashed_count_old = 0
  flashed = np.zeros(grid.shape, dtype=np.bool)
  g = grid.copy()
  g += 1

  while flashed_count != flashed_count_old:
    flashed_count_old = flashed_count
    newflashes = np.logical_and(g>9, np.logical_not(flashed))
    flashed = np.logical_or(flashed, newflashes)
    # print('newflashes')
    # print(newflashes)

    propagated_energy = scipy.signal.convolve2d(newflashes, flash_conv, mode='same')
    # print('propagated_energy')
    # print(propagated_energy)

    g += propagated_energy
    # propagated_energy = np.logical_and(propagated_flashes, np.logical_not(flashed))

    flashed_count = np.sum(flashed)
  g[flashed] = 0

  return g, flashed


if __name__ == '__main__':
  main()