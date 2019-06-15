import json
import nim

HEAP_SIZE = 10

moves = {}
for a in range(HEAP_SIZE, 0, -1):
    for b in range(HEAP_SIZE, 0, -1):
        for c in range(HEAP_SIZE, 0 , -1):
          moves[f'{a}.{b}.{c}'] = nim.nim([a, b , c], nim.NORMAL, False)

print(json.dumps(moves, indent=4, separators=(',', ': ')))
