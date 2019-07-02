import sys
from lib import nim, nimgraph

def build_sample(state, path):
    next_move = nim.nim(state, 'normal', False)
    nimgraph.draw_state(path, [9, 9, 9], state, next_move)


if __name__ == '__main__' and len(sys.argv) >= 2:
    build_sample([5, 3, 4], sys.argv[1])
