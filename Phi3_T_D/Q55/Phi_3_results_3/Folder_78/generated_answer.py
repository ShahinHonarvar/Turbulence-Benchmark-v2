def lists_with_product_equal_n(circular):
    result = []
    n = 74
    len_circular = len(circular)

    def dfs(index, current, prod):
        if prod == n:
            result.append(current[:-1])
            return
        if prod > n or index >= len_circular:
            return
        for next_index in (index + 1, index):
            if current and current[-1] == circular[next_index]:
                continue
            current.append(circular[next_index])
            prod *= circular[next_index]
            dfs(next_index, current, prod)
            current.pop()
            prod //= circular[next_index]
    if circular:
        start_dfs = dfs(-1, [], 1)
        end_dfs = dfs(len_circular - 1, [], 1)
        return start_dfs + end_dfs
    return result