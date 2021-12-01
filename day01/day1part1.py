with open('input.txt', 'r') as f:
  lines = f.readlines()
  lines = [l.strip() for l in lines]

numbers = [int(x) for x in lines]

increase_count = 0
for i in range(1, len(numbers)):
  if numbers[i] > numbers[i-1]:
    increase_count += 1

print(increase_count)
