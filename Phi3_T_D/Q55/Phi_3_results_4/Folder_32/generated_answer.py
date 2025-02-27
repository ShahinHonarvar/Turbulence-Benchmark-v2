def find_sublists_with_product(head, tail, target, product=1, sublists=None):
    if sublists is None:
        sublists = []
    if product == target and tail != head:
        sublists.append(list(head))
    if tail == head:
        return sublists
    if tail == -1 or product * tail > target:
        return sublists
    head.append(tail)
    find_sublists_with_product(head, (tail + 1) % len(lst), target, product * tail, sublists)
    head.pop()

def lists_with_product_equal_n(lst):
    n = 76
    return find_sublists_with_product([], -1, n)