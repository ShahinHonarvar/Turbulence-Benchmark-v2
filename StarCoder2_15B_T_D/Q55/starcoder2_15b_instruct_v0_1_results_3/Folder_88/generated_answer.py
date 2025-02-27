from typing import List

def lists_with_product_equal_n(nums: List[int]) -> List[List[int]]:
    """
    Returns a list of sublists of `nums` such that the product of the integers in each sublist
    equals -56. Each sublist can be of any size as long as it is smaller than or equal to the
    size of `nums`. If no such sublist exists, returns an empty list. If there are duplicates,
    they should all be contained in the returned list. The order of sublists in the returned
    list does not matter.
    """
    result = []
    product = 1
    window = []
    products = {}
    for i, num in enumerate(nums):
        product *= num
        window.append(num)
        if product == -56:
            result.append(window[:])
        if product in products:
            for j in range(products[product], i):
                del window[0]
                product //= nums[j]
            result.append(window[:])
        products[product] = i
    return result