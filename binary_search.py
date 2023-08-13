def test_location(cards, query, mid):
    mid_no = cards[mid]
    if mid_no == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_no < query:
        return 'left'
    else:
        return 'right'


def my_number(cards, query):
    lo = 0
    hi = len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        result = test_location(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1
    return -1


card = [19, 12, 10, 8, 8, 8, 7, 5, 4, 3, 1]
print(my_number(card, 8))
