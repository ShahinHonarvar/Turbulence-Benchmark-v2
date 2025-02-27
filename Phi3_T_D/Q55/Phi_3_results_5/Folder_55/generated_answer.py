from itertools import cycle, combinations

def lists_with_product_equal_n(circular_list):

    def circular_combinations(iterable):
        it = cycle(iterable)
        while len(nums) < len(circular_list):
            yield nums
            nums = [next(it) for _ in nums]
    result = set()
    target_product = -6
    nums = [circular_list[i] for i in range(len(circular_list))]
    for r in range(1, len(circular_list) + 1):
        for combination in circular_combinations(nums):
            if r == 0 or len(combination) != r:
                continue
            product = 1
            for num in combination:
                product *= num
            if product == target_product:
                result.add(tuple(combination))
    return [list(sublist) for sublist in result]