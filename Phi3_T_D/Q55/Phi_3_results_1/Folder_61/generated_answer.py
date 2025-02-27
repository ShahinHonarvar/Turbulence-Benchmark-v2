def lists_with_product_equal_n(lst):
    n = -10
    results = []

    def find_sublists(start, path):
        if start == len(lst):
            start = 0
        if lst[start] == 0:
            if start == 0 or all((item != 0 for item in path[1:])):
                results.append(path)
            return
        if n % lst[start]:
            find_sublists(start + 1, path + [lst[start]])
            find_sublists(start + 1, path)
        if not results and lst[start] == n:
            results.append(path + [lst[start]])
    find_sublists(0, [])
    return results