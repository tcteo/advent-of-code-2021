import numpy as np

def parse_input(input_filename):
  with open(input_filename, 'r') as f:
    lines = f.readlines()

  numbers = []
  boards = []
  current_board = []
  for linenum, line in enumerate(lines):
    line = line.strip()
    if linenum==0: # first line has the numbers
      numbers = line.split(',')
      numbers = [int(x) for x in numbers]
      continue
    elif linenum==1: # second line has the boards
      if line!='':
        raise
      continue
    
    # parsing a board
    if (linenum-2) % 6 == 5:
      if line!='':
        raise Exception(f'expecting empty line at line {linenum}, got: {line}')
      continue

    current_board_row = line.replace('  ', ' ').split(' ')
    current_board_row = [int(x) for x in current_board_row]
    assert len(current_board_row) == 5
    current_board.append(current_board_row)
    if len(current_board)==5:
      boards.append(current_board)
      current_board = []

  return numbers, np.array(boards)

def init_hits(boards):
  hits = np.zeros([len(boards), 5, 5], dtype=np.bool)
  return hits

def winning_boards(hits):
  # return indices of winning boards

  # sum by axis 2 (rows); any element with 5 = win
  row_sums = np.sum(hits, axis=2)
  row_win = row_sums >= 5
  boards_won_by_row = np.sum(row_win, axis=1) > 0

  # sum by axis 1 (columns); any element with 5 = win
  col_sums = np.sum(hits, axis=1)
  col_win = col_sums >= 5
  boards_won_by_col = np.sum(col_win, axis=1) > 0

  boards_won = (boards_won_by_row + boards_won_by_col) > 0



  return list(np.nonzero(boards_won))[0] # returns indices of elements >0

def board_unmarked_sum(boards, hits, board_index):
  b = boards[board_index].copy()
  h = hits[board_index].copy()
  b[h==True] = 0
  return np.sum(b)

def main():

  numbers,boards = parse_input('input.txt')
  # numbers,boards = parse_input('testdata.txt')
  print(f'{numbers=}')
  print(f'{boards=}')

  hits = init_hits(boards)
  wb = winning_boards(hits)
  print(f'initial state: {len(wb)} winning boards: {wb}')

  for num in numbers:
    print(num)
    hits_this_round = boards == num
    print(f'               {np.sum(hits_this_round)} hits this round')
    hits = hits + hits_this_round
    wb = winning_boards(hits)
    print(f'               {np.sum(hits)} hits total')
    print(f'               {len(wb)} winning boards: {wb}')
    if len(wb)>0:
      winning_board_unmarked_sum = board_unmarked_sum(boards, hits, wb[0])
      score = winning_board_unmarked_sum * num
      print(f'{score=}')
      break


if __name__ == '__main__':
  main()

