"""
nim playing
Adapted from:
https://en.wikipedia.org/w/index.php?title=Nim&oldid=896598086
"""

import functools

MISERE = 'misere'
NORMAL = 'normal'


def desperate_move(heaps):
    """
    Computes a move when all is lost and the only possibility is for the
    other player to make a mistake.

    The strategy is to remove one item from the first heap with elements.

    :param heaps:
    :return:
    """
    for index, heap in enumerate(heaps):
        if heap > 0:
            return index, 1
    return 0, 0


def nim(heaps, game_type, output=True):
    """
    Computes next move for Nim, for both game types normal and misere.

    if there is a winning move:
        return tuple(heap_index, amount_to_remove)
    else:
        return 0, 0

    - mid-game scenarios are the same for both game types

    >>> print(nim([1, 2, 3], MISERE))
    misere [1, 2, 3] (0, 0)
    >>> print(nim([1, 2, 3], NORMAL))
    normal [1, 2, 3] (0, 0)
    >>> print(nim([1, 2, 4], MISERE))
    misere [1, 2, 4] (2, 1)
    >>> print(nim([1, 2, 4], NORMAL))
    normal [1, 2, 4] (2, 1)


    - endgame scenarios change depending upon game type

    >>> print(nim([1], MISERE))
    misere [1] (0, 0)
    >>> print(nim([1], NORMAL))
    normal [1] (0, 1)
    >>> print(nim([1, 1], MISERE))
    misere [1, 1] (0, 1)
    >>> print(nim([1, 1], NORMAL))
    normal [1, 1] (0, 0)
    >>> print(nim([1, 5], MISERE))
    misere [1, 5] (1, 5)
    >>> print(nim([1, 5], NORMAL))
    normal [1, 5] (1, 4)

    """

    if output:
        print(game_type, heaps, end=' ')

    is_misere = game_type == MISERE

    count_non_0_1 = sum(1 for x in heaps if x > 1)
    is_near_endgame = (count_non_0_1 <= 1)

    # nim sum will give the correct end-game move for normal play but
    # misere requires the last move be forced onto the opponent
    if is_misere and is_near_endgame:
        moves_left = sum(1 for x in heaps if x > 0)
        is_odd = (moves_left % 2 == 1)
        sizeof_max = max(heaps)
        index_of_max = heaps.index(sizeof_max)

        if sizeof_max == 1 and is_odd:
            return desperate_move(heaps)

        # reduce the game to an odd number of 1's
        return index_of_max, sizeof_max - int(is_odd)

    nim_sum = functools.reduce(lambda x, y: x ^ y, heaps)
    if nim_sum == 0:
        return desperate_move(heaps)

    # Calc which move to make
    for index, heap in enumerate(heaps):
        target_size = heap ^ nim_sum
        if target_size < heap:
            amount_to_remove = heap - target_size
            return index, amount_to_remove


if __name__ == "__main__":
    import doctest
    doctest.testmod()
