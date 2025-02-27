def palindromes_between_indices(s):
    s = s[3:9]
    s = s.lower()
    letters = set(s)
    result = set()
    for length in range(7, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                result.add(''.join(perm))
    return result