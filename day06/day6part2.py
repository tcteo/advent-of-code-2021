import collections

def main():
  fish = parse_fish_input('input.txt')
  print(f'{len(fish)=}')

  for i in range(0,256):
    fish = sim_fish(fish)

  total_fish_count = sum(fish.values())
  print(f'{total_fish_count=}')

def parse_fish_input(input_filename):
  with open(input_filename, 'r') as f:
    fish = [int(x) for x in f.readlines()[0].strip().split(',')]

  fish_count_by_timer = collections.defaultdict(int)
  for f in fish:
    fish_count_by_timer[f] += 1
  return fish_count_by_timer


NEW_FISH_TIMER = 8
RESET_TIMER = 6

def sim_fish(fish_count_by_timer):
  new_fish_count_by_timer = collections.defaultdict(int)
  for t in range(0,9):
    if t==0:
      # each of these spawns a new fish
      new_fish_count_by_timer[NEW_FISH_TIMER] += fish_count_by_timer[t]
      # all of these get reset
      new_fish_count_by_timer[RESET_TIMER] += fish_count_by_timer[t]
    else:
      new_fish_count_by_timer[t-1] += fish_count_by_timer[t]
  return new_fish_count_by_timer

if __name__ == '__main__':
  main()
