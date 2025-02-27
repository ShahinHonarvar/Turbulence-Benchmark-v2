def lists_with_product_equal_n(nums):

    def product_sublists(index, product, current, result):
        if product == -968:
            result.append(current.copy())
        for i in range(len(nums)):
            new_index = (index + i) % len(nums)
            if new_index < len(nums):
                product *= nums[new_index]
                current.append(nums[new_index])
                if product != 0 and -968 % product == 0:
                    product_sublists(new_index + 1, product, current, result)
                current.pop()
                product //= nums[new_index]
            else:
                break
    result = []
    product_sublists(0, 1, [], result)
    return result