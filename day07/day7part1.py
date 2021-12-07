import numpy as np

def main():
  # positions = parse_input('test.txt')
  positions = parse_input('input.txt')
  positions = np.array(positions, dtype=np.int32)
  # print(positions)

  min_pos = np.min(positions)
  max_pos = np.max(positions)
  min_fuel = None
  min_fuel_sum = None
  min_fuel_pos = None
  for pos in range(min_pos, max_pos+1):
    fuel = np.abs(positions-pos)
    fuel_sum = np.sum(fuel)
    # print(f'{pos=}, {fuel_sum=}')
    if min_fuel_sum is None or fuel_sum < min_fuel_sum:
      min_fuel_pos = pos
      min_fuel_sum = fuel_sum
      min_fuel = fuel
  print(f'{min_fuel_pos=}')
  print(f'{min_fuel=}')
  print(f'{min_fuel_sum=}')

  # wrong: 364625, too high

def parse_input(infile):
  with open(infile, 'r') as f:
    positions = f.readlines()[0].strip().split(',')
    return positions

if __name__ == '__main__':
  main()
