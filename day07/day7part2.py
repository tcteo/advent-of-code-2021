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
    move_dist = np.abs(positions-pos)
    move_dist = np.sort(move_dist) # sorting doesnt change the total distance, but makes memoization more efffffficient
    fuel = np.array([fuel_for_move(x) for x in move_dist])
    fuel_sum = np.sum(fuel)
    # print(f'{pos=}, {fuel_sum=}')
    if min_fuel_sum is None or fuel_sum < min_fuel_sum:
      min_fuel_pos = pos
      min_fuel_sum = fuel_sum
      min_fuel = fuel
  print(f'{min_fuel_pos=}')
  print(f'{min_fuel=}')
  print(f'{min_fuel_sum=}')


memo = {}

def fuel_for_move(dist):
  sum = 0
  for i in range(dist, 0, -1):
    if i in memo:
      sum += memo[i]
      break
    else:
      sum += i
  memo[dist] = sum
  return sum  


def parse_input(infile):
  with open(infile, 'r') as f:
    positions = f.readlines()[0].strip().split(',')
    return positions

if __name__ == '__main__':
  main()
