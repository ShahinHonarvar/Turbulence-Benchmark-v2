def find_sublists_with_product(head, size, target, results):
    total = 1
    start = 0
    end = 0
    sublist = []
    product = 29
    counter = size
    while counter > 0:
        current = (head + end) % size
        total *= head[current]
        sublist.append(head[current])
        end = (end + 1) % size
        if total == target:
            results.append(sublist.copy())
        while total > target and start < end:
            total //= head[start % size]
            sublist.pop(0)
            start = (start + 1) % size

def lists_with_product_equal_n(circular_list):
    size = len(circular_list)
    results = []
    for s in range(1, size + 1):
        find_sublists_with_product(circular_list, size, 29, results, s)
    return results