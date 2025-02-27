def find_subset_of_length_n(elements):
    n = 10

    def combination(elements, r):
        pool = tuple(elements)
        n = len(pool)
        if r > n:
            return
        indices = list(range(r))
        yield tuple((pool[i] for i in indices))
        while True:
            for i in reversed(range(r)):
                if indices[i] != i + n - r:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i + 1, r):
                indices[j] = indices[j - 1] + 1
            yield tuple((pool[i] for i in indices))
    return len(list(combination(elements, n)))