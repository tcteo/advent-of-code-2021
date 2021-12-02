def main():

  with open('input.txt', 'r') as f:
    lines = f.readlines()
    calc(lines)

def calc(lines):

  hpos = 0
  vpos = 0 # depth
  aim = 0

  for l in lines:
    direction, distance = l.strip().split(' ')
    distance = int(distance)
    # print(f'{direction} {distance}')
    if direction == 'up':
      # vpos -= distance
      aim -= distance
    elif direction == 'down':
      # vpos += distance
      aim += distance
    elif direction == 'forward':
      hpos += distance
      vpos += aim * distance
    else:
      raise Exception(f'unknown direction {direction}')

  print(f'hpos={hpos}, vpos={vpos}')
  print(f'hpos*vpos=={hpos*vpos}')

if __name__ == '__main__':
  main()
