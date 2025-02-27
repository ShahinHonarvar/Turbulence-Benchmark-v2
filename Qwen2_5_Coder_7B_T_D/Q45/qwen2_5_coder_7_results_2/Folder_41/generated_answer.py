def palindromes_between_indices(s):
    subset = set(s[2:4])
    lower_subset = subset.lower()
    result = set()
    for i in range(len(lower_subset)):
        for j in range(i + 3, len(lower_subset) + 1):
            candidate = lower_subset[i:j]
            if candidate == candidate[::-1]:
                result.add(candidate.upper())
    return result