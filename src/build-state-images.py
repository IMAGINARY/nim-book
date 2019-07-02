import sys
import os
from lib import nim, nimgraph

def build_images(outdir):
    for a in range(10):
        for b in range(10):
            for c in range(10):
                next_move = nim.nim([a, b, c], 'normal', False)
                nimgraph.draw_state(os.path.join(outdir, f'{a}-{b}-{c}.svg'), [9, 9, 9], [a, b, c], next_move)



if __name__ == '__main__' and len(sys.argv) >= 2:
    build_images(sys.argv[1])
