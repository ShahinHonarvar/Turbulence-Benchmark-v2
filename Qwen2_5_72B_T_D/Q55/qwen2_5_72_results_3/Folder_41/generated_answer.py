def lists_with_product_equal_n(nums):

    def get_sublists(lst, target_product=-20):
        n = len(lst)
        result = []
        for start in range(n):
            product = 1
            for end in range(start, start + n):
                product *= lst[end % n]
                if product == target_product:
                    result.append(lst[start:end % n + 1])
                elif abs(product) > abs(target_product):
                    break
        return result
    return get_sublists(nums)