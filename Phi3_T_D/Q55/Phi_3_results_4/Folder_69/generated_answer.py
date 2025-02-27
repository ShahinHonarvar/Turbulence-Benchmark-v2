def lists_with_product_equal_n(circular_list):
    nums = circular_list + circular_list
    result = []
    n = 90
    factors = [i for i in range(1, int(n ** 0.5) + 1) if n % i == 0]
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + i):
            subset = nums[i:j]
            product = 1
            for num in subset:
                product *= num
            if product == n:
                result.append(subset)
    return result