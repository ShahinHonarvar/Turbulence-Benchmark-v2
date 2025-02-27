def lists_with_product_equal_n(circular_list):

    def sublists_with_product(circular_list, required_product):
        n = len(circular_list)
        result = []
        for start in range(n):
            product = 1
            for end in range(start, start + n):
                product *= circular_list[end % n]
                if product == required_product:
                    result.append(circular_list[start:end % n + 1])
                elif product < required_product * -1:
                    break
        return result
    return sublists_with_product(circular_list, -18)