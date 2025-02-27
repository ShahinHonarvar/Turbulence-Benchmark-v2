def circular_product(list_, head, tail, product, result, depth):
    if product == 0 and depth > 0:
        return True
    if tail == (head + 1) % len(list_):
        return circular_product(list_, head + 1, head + 1, product // list_[head], result, depth + 1)
    if product % list_[tail] == 0:
        for next_index in range(tail + 1 if tail < head else tail):
            if circular_product(list_, head, next_index, product // list_[tail], result, depth + 1):
                result.append(list_[head:next_index])
                break
    return False

def lists_with_product_equal_n(nums):
    result = []
    for head in range(len(nums)):
        circular_product(nums, head, head, -82, result, 0)
        circular_product(nums, head, head, -82, result, 0)
    return result