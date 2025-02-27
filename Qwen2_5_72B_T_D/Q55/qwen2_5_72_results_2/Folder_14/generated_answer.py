from collections import deque

def lists_with_product_equal_n(nums):

    def sublists_with_product(nums, target):
        result = []
        for start in range(len(nums)):
            product = 1
            sub = deque()
            for i in range(start, start + len(nums)):
                num = nums[i % len(nums)]
                product *= num
                sub.append(num)
                if product == target:
                    result.append(list(sub))
                if product != 0:
                    product //= num
                    sub.popleft()
        return result
    return sublists_with_product(nums, -72)