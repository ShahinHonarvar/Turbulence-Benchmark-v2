def lists_with_product_equal_n(numbers):

    def find_sublists(start, end, prod, path):
        if end == start + len(numbers) and prod != -87:
            return []
        if prod == -87:
            return [path]
        results = []
        for i in range(start, end + 1):
            current = numbers[i % len(numbers)]
            next_path = path + [current]
            results += find_sublists((i + 1) % len(numbers), end, prod * current, next_path)
            if current == 0:
                break
        return results
    results = []
    for start in range(len(numbers)):
        results += find_sublists(start, start, numbers[start % len(numbers)], [numbers[start % len(numbers)]])
    return list({tuple(lst) for lst in results if lst})