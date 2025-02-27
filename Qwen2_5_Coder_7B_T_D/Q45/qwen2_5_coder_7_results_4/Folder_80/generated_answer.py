def palindromes_between_indices(s):
    subset = s[3:9]
    letters = sorted(set(subset.lower()))
    n = len(letters)
    result = set()
    for i in range(n):
        for j in range(i, n):
            for k in range(j, n):
                for l in range(k, n):
                    for m in range(l, n):
                        for o in range(m, n):
                            for p in range(o, n):
                                for q in range(p, n):
                                    candidate = letters[i] + letters[j] + letters[k] + letters[l] + letters[m] + letters[o] + letters[p] + letters[q]
                                    if candidate == candidate[::-1]:
                                        result.add(candidate)
    return result