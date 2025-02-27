def lists_with_product_equal_n(circular_list):
    if not circular_list:
        return []
    product = -18
    target = tuple(product_factors(product))
    valid_sublists = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list) + i):
            sublist = circular_list[i % len(circular_list):j % len(circular_list) + 1]
            if tuple(product(sublist)) == target:
                if sublist not in valid_sublists:
                    valid_sublists.append(sublist)
    return valid_sublists

def product(lst):
    result = 1
    for num in lst:
        if num == 0:
            result = 0
            break
        result *= num
    return result

def product_factors(n):
    factors = []
    for i in range(2, abs(n) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    return factors or [1] if n == 1 else []