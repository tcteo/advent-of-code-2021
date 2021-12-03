import numpy as np

def main():

  with open('input.txt', 'r') as f:
    lines = f.readlines()
  bits = [
    np.array([1 if x=='1' else 0 for x in list(line.strip())])
    for line in lines
  ]
  print(bits)


  bitlen = len(bits[0])
  sums = np.zeros(bitlen)
  
  for i in range(0,len(bits)):
    sums += bits[i]

  print(f'{sums=}')

  denominator = len(bits)
  print(f'{denominator=}')
  gamma_bits = sums>(denominator/2)
  epsilon_bits = sums<(denominator/2)
  err_equal = sums==(denominator/2)
  print(f'{gamma_bits=}')
  print(f'{epsilon_bits=}')
  # print(f'{err_equal=}')

  if any(err_equal):
    raise Exception('some bits had equal 1s and 0s')

  gamma = np_binary_array_to_int(gamma_bits)
  epsilon = np_binary_array_to_int(epsilon_bits)
  print(f'{gamma=}')
  print(f'{epsilon=}')
  print(f'gamma*epsilon = {gamma*epsilon}')

def np_binary_array_to_int(a):
  sum = 0
  while len(a)>0:
    sum *= 2
    if a[-1]:
      sum += 1 
    a = a[:-1]
  return sum

if __name__ == '__main__':
  main()
