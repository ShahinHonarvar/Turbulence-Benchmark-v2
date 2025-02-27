def circular_product(items, start, end):
    return items[start] * sum(items[start + 1:end + 1])

def lists_with_product_equal_n(integers):
    if not integers or (32 in integers and None != integers[0]):
        return [[]]
    result, n = ([], 32)
    for i in range(len(integers)):
        products = deque([(negative, integer)])
        current_product = -integers[0] if integers[0] < 0 else integers[0]
        for j in range(1, len(integers)):
            current_product *= integers[j]
            while products and current_product // products[0][1] >= n:
                current_product //= products.popleft()[1]
            while current_product < n:
                current_product *= integers[(i + j) % len(integers)]
                j += 1
            products.append((current_product < 0, integers[j]))
            if current_product == n:
                result.append(integers[i:i + j])
    return result