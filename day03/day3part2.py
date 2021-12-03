import numpy as np

def main():

  with open('input.txt', 'r') as f:
    lines = f.readlines()

#   # test data
#   lines = '''00100
# 11110
# 10110
# 10111
# 10101
# 01111
# 00111
# 11100
# 10000
# 11001
# 00010
# 01010'''.split('\n')

  bits = [
    np.array([1 if x=='1' else 0 for x in list(line.strip())], dtype=np.int32)
    for line in lines
  ]
  print(bits)

  bitlen = len(bits[0])
  print(f'{bitlen=}')

  o2rating = bits.copy()
  co2rating = bits.copy()

  for i in range(0,bitlen):
    o2sums = np.sum(o2rating, axis=0)
    if o2sums[i] >= len(o2rating)/2: # 1 is more common, or equal
      keep = 1
      print('keep1')
    else: # 0 is more common
      keep = 0
      print('keep0')
    o2rating = [x for x in o2rating if x[i]==keep]
    print(f'{i=}, {len(o2rating)=}')
    if len(o2rating)==1:
      break
  assert len(o2rating)==1
  o2_value = np_binary_array_to_int(o2rating[0])
  print(f'{o2rating[0]=}')
  print(f'{o2_value=}')

  for i in range(0,bitlen):
    co2sums = np.sum(co2rating, axis=0)
    if co2sums[i] >= len(co2rating)/2: # 1 is more common
      keep = 0
      print('keep0')
    else: # 0 is more common, or equal
      keep = 1
      print('keep1')
    co2rating = [x for x in co2rating if x[i]==keep]
    print(f'{i=}, {len(co2rating)=}')
    if len(co2rating)==1:
      break
  assert len(co2rating)==1
  co2_value = np_binary_array_to_int(co2rating[0])
  print(f'{co2rating[0]=}')
  print(f'{co2_value=}')

  life_support_rating = o2_value*co2_value
  # wrong answers
  assert life_support_rating != 10221282 # too high
  print(f'{life_support_rating=}')

def np_binary_array_to_int(a):
  sum = 0
  for ai in a:
    sum *= 2
    sum += ai
  return sum

if __name__ == '__main__':
  main()
