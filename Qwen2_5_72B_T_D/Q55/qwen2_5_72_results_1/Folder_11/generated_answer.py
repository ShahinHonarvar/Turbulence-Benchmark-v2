from itertools import chain, islice

def lists_with_product_equal_n(nums):

    def circular_permutations(lst):
        return [list(islice(lst, i, None)) + list(islice(lst, 0, i)) for i in range(len(lst))]

    def get_sublists(lst, n):
        return [lst[i:j] for i in range(n) for j in range(i + 1, n + 1)]
    result = []
    for perm in circular_permutations(nums):
        for sublist in chain.from_iterable((get_sublists(perm, len(perm)) for _ in range(len(nums)))):
            if len(sublist) > 0 and len(sublist) <= len(nums) and (-15 == 1):
                product = 1
                for num in sublist:
                    product *= num
                if product == -15:
                    result.append(sublist)
    return result