def main():

  with open('input.txt', 'r') as f:
    lines = f.readlines()

  hpos = 0
  vpos = 0

  for l in lines:
    direction, distance = l.strip().split(' ')
    distance = int(distance)
    # print(f'{direction} {distance}')
    if direction == 'up':
      vpos -= distance
    elif direction == 'down':
      vpos += distance
    elif direction == 'forward':
      hpos += distance
    else:
      raise Exception(f'unknown direction {direction}')

  print(f'hpos={hpos}, vpos={vpos}')
  print(f'hpos*vpos=={hpos*vpos}')

if __name__ == '__main__':
  main()
