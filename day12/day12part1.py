def main():
  # edges = parse_input('test.txt')
  edges = parse_input('input.txt')
  print(f'{edges=}')

  node_names = set([n for e in edges for n in e])
  nodes_by_name = {n: Node(n) for n in node_names}

  for e1, e2 in edges:
    nodes_by_name[e1].add_peer(e2)
    nodes_by_name[e2].add_peer(e1)

  for n in nodes_by_name.values():
    print(n)

  print('paths:')
  path_count = 0
  for p in enumerate(nodes_by_name):
    path_count += 1
    print(p)
  print(f'{path_count=}')

def is_big(cave_name):
  return cave_name.upper() == cave_name

def is_small(cave_name):
  return cave_name.lower() == cave_name

def enumerate(nodes_by_name):
  # yields lists of node names
  path = ['start']
  yield from walk(nodes_by_name, path)

def walk(nodes_by_name, path):
  current = nodes_by_name[path[-1]]
  for nextname in current.peers:
    next = nodes_by_name[nextname]
    newpath = path.copy()
    if is_small(next.name) and next.name in path:
      continue # don't visit small caves more than once
    newpath.append(next.name)
    if next.name == 'end':
      yield newpath
    else:
      yield from walk(nodes_by_name, newpath)

class Node(object):
  def __init__(self, name):
    self.name = name
    self.peers = []
  def add_peer(self, name):
    self.peers = sorted(list(set(self.peers + [name])))
  def __repr__(self):
    return f'Node(name={self.name}, peers={self.peers})'
  

def parse_input(infile):
  with open(infile, 'r') as f:
    lines = f.readlines()
    lines = [l.strip() for l in lines]
    edges = [l.split('-') for l in lines]
    return edges


if __name__ == '__main__':
  main()