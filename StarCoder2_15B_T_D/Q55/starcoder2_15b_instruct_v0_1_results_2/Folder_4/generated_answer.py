def lists_with_product_equal_n(lst: list, n: int) -> list:
    result = []

    def helper(idx: int, prod: int, sublst: list):
        if idx == len(lst) and prod == n:
            result.append(sublst)
        elif idx < len(lst):
            helper(idx + 1, prod * lst[idx], sublst + [lst[idx]])
            helper(idx + 1, prod, sublst)
    helper(0, 1, [])
    return result