import svgwrite

ITEM_SIZE = 30
ITEM_STROKE = 3.5
ITEM_SPACING = 5
HEAP_SPACING = 25 + ITEM_STROKE
TEXT_HEIGHT = 30
TEXT_MARGIN = 2
SUGGESTION_SIZE = 6

STROKE_COLOR = 'black'
BASE_COLOR = 'white'
REMOVED_COLOR = '#999'

def create_tile(dwg, x, y, size):
    return dwg.rect(insert=(x, y), size=(size, size))\
        .fill(REMOVED_COLOR)


def create_magnet(dwg, x, y, size):
    radius = size / 2 - ITEM_STROKE
    return dwg.circle(center=(x + radius + ITEM_STROKE, y + radius + ITEM_STROKE), r=radius)\
        .fill(BASE_COLOR)\
        .stroke(STROKE_COLOR, width=ITEM_STROKE)


def create_heap(dwg, size, items_left, suggestion=None):
    group = dwg.g()
    for i in range(size):
        y = i * (ITEM_SIZE + ITEM_SPACING) + ITEM_SPACING
        removed = i >= items_left
        group.add(create_tile(dwg, 0, y, ITEM_SIZE))
        if (not removed):
            group.add(create_magnet(dwg, 0, y, ITEM_SIZE))
            if suggestion is not None and (items_left - suggestion) <= i < items_left:
                group.add(
                    dwg.text(
                        text='×',
                        insert=(ITEM_SIZE - ITEM_STROKE * 0.5, y + TEXT_HEIGHT * 0.9),
                        style=f'font-family: \'Futura PRO Book\'; font-weight: bold; font-size: {TEXT_HEIGHT}px; text-anchor: left;'
                    )
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

    dwg = svgwrite.Drawing(outpath, profile='full', viewBox="-20 0 200 350", preserveAspectRatio="xMidYMid meet", size=('200', '350'))

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
