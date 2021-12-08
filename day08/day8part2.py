import numpy as np
from collections import namedtuple
import itertools

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

  sum = 0
  for sample in samples:
    d = solve_sample(sample)
    print(d)
    sum += d
  print(f'{sum=}')


digit_to_segments = [
  'abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf',
  'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg'
]
#     aaaa 
#    b    c
#    b    c
#     dddd
#    e    f
#    e    f
#     gggg 
segments_to_digits = {}
for d,s in enumerate(digit_to_segments):
  segments_to_digits[s] = d

def remove_candidate(ss, s):
  return ''.join([x for x in list(ss) if x!=s])
def filter_candidates(ss, sfilter):
  return ''.join([x for x in list(ss) if x in sfilter])
def ss(s): # sort chars in a string
  assert type(s)==str
  return ''.join(sorted(s))

def sig_seg_solved(sig_seg):
  return np.all(np.sum(sig_seg, axis=1) == 1)

segletters = ['a','b','c','d','e','f','g']
segment_permutations = list(itertools.permutations(segletters))
# 7P7 = 5040 permutations, which is small enough to bruteforce

def solve_sample(sample):
  # try each segment permutation, find candidate permutations
  candidate_permutations = []
  for sp in segment_permutations:
    eliminate = False
    spmap = dict(zip(segletters, sp)) # input to output map
    # spmapinv = dict(zip(sp, segletters)) # output to input map
    for sig in sample.signals:
      # check that all signals form valid digits with this permutation
      # if not, discard
      mapped_sig = ''.join(sorted([spmap[c] for c in sig]))
      if not mapped_sig in digit_to_segments:
        eliminate = True
        continue
    if not eliminate:
      candidate_permutations.append(sp)

  if len(candidate_permutations) != 1:
    print(f'{candidate_permutations=}')
    raise Exception('len(candidate_permutations!=1)')

  sp = candidate_permutations[0]
  spmap = dict(zip(segletters, sp)) # input to output map
  # spmapinv = dict(zip(sp, segletters)) # output to input map
  digits = []
  for sig in sample.outputs:
    # invmapped_sig = ''.join(sorted([spmapinv[c] for c in sig]))
    mapped_sig = ''.join(sorted([spmap[c] for c in sig]))
    digit = segments_to_digits[mapped_sig]
    digits.append(digit)
  return int(''.join([str(x) for x in digits]))


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