def main():
  fish = parse_fish_input('input.txt')
  print(f'{len(fish)=}')

  for i in range(0,80):
    fish = sim_fish(fish)
  print(f'{len(fish)=}')

def parse_fish_input(input_filename):
  with open(input_filename, 'r') as f:
    fish = [int(x) for x in f.readlines()[0].strip().split(',')]
  return fish


NEW_FISH_TIMER = 8
RESET_TIMER = 6

def sim_fish(fish):
  new_fish = []
  for i in range(0,len(fish)):
    if fish[i] == 0:
      new_fish.append(NEW_FISH_TIMER)
      fish[i] = RESET_TIMER
    else:
      fish[i] -= 1

  return fish + new_fish

if __name__ == '__main__':
  main()
