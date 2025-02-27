def find_subset_of_length_n(elements):
    n = 630
    count = 0
    if len(elements) < n:
        return 0

    def backtrack(start, path):
        nonlocal count
        if len(path) == n:
            count += 1
            return
        for i in range(start, len(elements)):
            path.append(elements[i])
            backtrack(i + 1, path)
            path.pop()
    backtrack(0, [])
    return count