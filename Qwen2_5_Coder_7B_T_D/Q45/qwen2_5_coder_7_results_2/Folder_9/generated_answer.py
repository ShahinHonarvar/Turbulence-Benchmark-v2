def palindromes_between_indices(s):
    result = set()
    for i in range(len(s)):
        for j in range(i + 7, len(s) + 1):
            subset = ''.join(sorted(s[i:j]))
            if subset == subset[::-1]:
                result.add(subset)
    return result