import svgwrite

ITEM_SIZE = 30
ITEM_STROKE = 5
ITEM_SPACING = 0
ITEM_SHAPE = 'square'  # circle | square
HEAP_SPACING = 25 + ITEM_STROKE
TEXT_HEIGHT = 20
TEXT_MARGIN = 2
SUGGESTION_SIZE = 6

STROKE_COLOR = 'black'
BASE_COLOR = 'white'
REMOVED_COLOR = '#999'


def create_square_item(dwg, x, y, size, removed):
    return dwg.rect(insert=(x, y), size=(size, size))\
        .fill(REMOVED_COLOR if removed else BASE_COLOR)\
        .stroke(STROKE_COLOR, width=ITEM_STROKE)


def create_round_item(dwg, x, y, size, removed):
    return dwg.circle(center=(x + size / 2, y + size / 2), r=size / 2)\
        .fill(REMOVED_COLOR if removed else BASE_COLOR)\
        .stroke(STROKE_COLOR, width=ITEM_STROKE)


def create_heap_item(dwg, shape, x, y, size, removed):
    if shape == 'square':
        return create_square_item(dwg, x, y, size, removed)
    else:
        return create_round_item(dwg, x, y, size, removed)


def create_heap(dwg, size, items_left, suggestion=None):
    group = dwg.g()
    for i in range(size):
        y = i * (ITEM_SIZE + ITEM_SPACING)
        removed = (size - i) <= (size - items_left)
        group.add(create_heap_item(dwg, ITEM_SHAPE, ITEM_STROKE, y, ITEM_SIZE, removed))
        if suggestion is not None and (items_left - suggestion) <= i < items_left:
            group.add(
                dwg.polygon([
                    [ITEM_SIZE + ITEM_STROKE * 1.5, y + ITEM_SIZE / 2],
                    [ITEM_SIZE + ITEM_STROKE * 2 + SUGGESTION_SIZE * 2, y + ITEM_SIZE / 2 + SUGGESTION_SIZE * 2],
                    [ITEM_SIZE + ITEM_STROKE * 2 + SUGGESTION_SIZE * 2, y + ITEM_SIZE / 2 - SUGGESTION_SIZE * 2],
                ])
                .fill(STROKE_COLOR)
            )
    return group


def draw_state(outpath, heap_sizes, heap_states, suggestion):
    """
    Draws a state of the game Nim
    :param heap_sizes: Max sizes of the heaps
    :param heap_states: The current number of elements in each heap
    :param suggestion: The suggested move as a (heap ID, amount) tuple
    """
    # heapSizes and heapStates must have the same size
    assert len(heap_sizes) == len(heap_states)
    # Every heap must have a number of elements less or equal to the size of the heap
    assert all(map(lambda a_b: a_b[0] >= a_b[1], zip(heap_sizes, heap_states)))

    dwg = svgwrite.Drawing(outpath, profile='full', viewBox="0 0 170 300", preserveAspectRatio="xMaxYMax meet")

    suggested_heap, suggested_amount = suggestion
    baseline = TEXT_HEIGHT + TEXT_MARGIN + (max(heap_sizes) * (ITEM_SIZE + ITEM_SPACING)) - ITEM_SPACING + ITEM_STROKE
    for i, (heap_size, heap_state) in enumerate(zip(heap_sizes, heap_states)):
        dwg.add(
            dwg.text(
                text=str(heap_state),
                insert=(i * (ITEM_SIZE + HEAP_SPACING) + ITEM_STROKE + (ITEM_SIZE / 2), TEXT_HEIGHT),
                style=f'font-family: \'Futura PRO Book\'; font-weight: bold; font-size: {TEXT_HEIGHT}px; text-anchor: middle;'
            )
        )
        heap = create_heap(dwg, heap_size, heap_state, suggested_amount if i == suggested_heap else None)
        heap.translate(
            tx=i * (ITEM_SIZE + HEAP_SPACING),
            ty=baseline - heap_size * (ITEM_SIZE + ITEM_SPACING)
        )
        dwg.add(heap)
    dwg.save()


if __name__ == "__main__":
    draw_state('test.svg', [10, 10, 10], [5, 3, 6], [1, 2])
