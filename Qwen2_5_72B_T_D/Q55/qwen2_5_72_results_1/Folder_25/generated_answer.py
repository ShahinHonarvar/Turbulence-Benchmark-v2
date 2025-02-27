def lists_with_product_equal_n(circular_list):

    def sublists_with_product(lst, product):
        n = len(lst)
        result = []
        for start in range(n):
            for end in range(1, n + 1):
                if start == 0 and end > n:
                    break
                if end <= start:
                    end += n
                current_product = 1
                for i in range(start, end):
                    current_product *= lst[i % n]
                if current_product == product:
                    result.append(lst[start:end])
        return result
    return sublists_with_product(circular_list, -32)