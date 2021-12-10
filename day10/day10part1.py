def main():
  lines = parse_input('input.txt')
  # lines = parse_input('test.txt')
  total_corruption_score = 0
  for s in lines:
    corruption_score = validate(s)
    total_corruption_score += corruption_score
  print(f'{total_corruption_score=}')

open2close = {
  '(':')',
  '[':']',
  '{':'}',
  '<':'>',
}
close2open = {
  v: k for k, v in open2close.items()
}
corruption_score_map = {
  ')':3,']':57,'}':1197,'>':25137
}

def validate(s):
  # print(s)
  stack = []
  for c in s:
    # open
    if c in '([{<':
      stack.append(c) # push
    elif c in ')]}>':
      if stack[-1] != close2open[c]:
        # stop at first illegal char
        return corruption_score_map[c]
      stack = stack[:-1] # pop
    else:
      raise Exception(f'unexpected char {c}')
  # corruption_score 0 for no errors
  # TODO handle incomplete lines
  return 0

def parse_input(infile):
  with open(infile, 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    return lines

if __name__ == '__main__':
  main()