def palindromes_between_indices(s):
    subset = s[3:9]
    subset = subset.lower()
    subset = ''.join(sorted(set(subset)))
    n = len(subset)
    result = set()
    for i in range(n - 5):
        for j in range(i + 5, n + 1):
            if subset[i:j] == subset[i:j][::-1]:
                result.add(subset[i:j])
    return result