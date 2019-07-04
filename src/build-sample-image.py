import sys
from lib import nim, nimgraph_stacks

def build_sample(state, path):
    next_move = nim.nim(state, 'normal', False)
    nimgraph_stacks.draw_state(path, [9, 9, 9], state, next_move)


if __name__ == '__main__' and len(sys.argv) >= 2:
    build_sample([9, 4, 3], sys.argv[1])
