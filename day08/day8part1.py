from collections import namedtuple

InEntry = namedtuple('InEntry', ['signals', 'outputs'])

segment_count_by_digit = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
unique_segment_count_to_digit = {
  2: 1,
  3: 7,
  4: 4,
  7: 8,
}

def main():
  # positions = parse_input('test.txt')
  samples = parse_input('input.txt')
  # print(samples)

  unique_output_count = 0
  for s in samples:
    for o in s.outputs:
      if len(o) in unique_segment_count_to_digit:
        unique_output_count += 1
  print(f'{unique_output_count=}')

def parse_input(infile):
  samples = []
  with open(infile, 'r') as f:
    lines = [l.strip() for l in f.readlines()]
    for line in lines:
      signals, outputs = line.split('|')
      signals = signals.strip()
      outputs = outputs.strip()
      signals = signals.split(' ')
      outputs = outputs.split(' ')
      samples.append(InEntry(signals, outputs))
    return samples

if __name__ == '__main__':
  main()