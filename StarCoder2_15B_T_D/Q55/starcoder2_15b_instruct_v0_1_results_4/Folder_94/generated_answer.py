from collections import deque

def lists_with_product_equal_n(lst):
    queue = deque(lst)
    sublists = []
    while True:
        curr_product = 1
        curr_list = []
        for num in queue:
            curr_product *= num
            curr_list.append(num)
            if curr_product == -30:
                sublists.append(curr_list)
            if curr_product == -30 and len(queue) > 1:
                queue.rotate(-1)
                break
        if len(queue) == 1:
            break
        queue.rotate(-1)
    return sublists