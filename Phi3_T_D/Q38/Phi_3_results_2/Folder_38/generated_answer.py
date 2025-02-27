def find_subset_of_length_n(elements):
    n = 38

    def combinations(subset, idx, n, results, buffer):
        if n == 0:
            results.add(tuple(buffer))
            return
        for i in range(idx, len(subset)):
            combinations(subset, i + 1, n - 1, results, buffer + [subset[i]])
    results = set()
    combinations(elements, 0, n, results, [])
    return len(results)