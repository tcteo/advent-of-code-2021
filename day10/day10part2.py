import numpy as np

def main():
  lines = parse_input('input.txt')
  # lines = parse_input('test.txt')
  acscores = []
  for i, s in enumerate(lines):
    ac = autocomplete(s)
    print(f'line {i} ac={ac}')
    if ac is not None:
      acscores.append(ac)
  median_ac = np.median(np.array(acscores, dtype=np.int64))
  print(f'{median_ac=}')

open2close = {
  '(':')',
  '[':']',
  '{':'}',
  '<':'>',
}
close2open = {
  v: k for k, v in open2close.items()
}
autocomplete_score_map = {
  ')':1,']':2,'}':3,'>':4
}


def autocomplete(s):
  # print(s)
  stack = []
  for c in s:
    # open
    if c in '([{<':
      stack.append(c) # push
    elif c in ')]}>':
      if stack[-1] != close2open[c]:
        # corrupted line, don't autocomplete
        return None
      stack = stack[:-1] # pop
    else:
      raise Exception(f'unexpected char {c}')
  if len(stack)==0:
    # the line was complete
    return None
  # autocompletion is the stack in reverse order
  acscore = 0
  for c in stack[::-1]:
    acscore *= 5
    acscore += autocomplete_score_map[open2close[c]]
  return acscore


def parse_input(infile):
  with open(infile, 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines

if __name__ == '__main__':
  main()