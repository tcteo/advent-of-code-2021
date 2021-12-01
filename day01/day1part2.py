
def windowed_sums(numbers, window_size=3):
  # numbers needs to be a list so we can look back
  # TODO: would be nice if it could take an iterator, though
  i = 0
  while i<len(numbers):
    if i-window_size+1>=0:
      yield sum(numbers[i-window_size+1:i+1])
    i += 1

with open('input.txt', 'r') as f:
  lines = f.readlines()
  lines = [l.strip() for l in lines]

numbers = [int(x) for x in lines]

prev = None
increase_count = 0
for w in windowed_sums(numbers):
  if prev is not None:
    if w > prev:
      increase_count += 1
  prev = w

print(increase_count)
