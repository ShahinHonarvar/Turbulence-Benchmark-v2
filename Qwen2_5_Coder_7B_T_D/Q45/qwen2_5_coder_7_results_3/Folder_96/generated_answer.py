def palindromes_between_indices(s):
    range_str = s[3:9]
    range_str = range_str.lower()
    letters = set(range_str)
    result = set()
    for i in range(len(range_str)):
        for j in range(i + 6, len(range_str) + 1):
            substring = range_str[i:j]
            if substring == substring[::-1] and len(substring) >= 6:
                permutations = set(permutations(substring))
                for perm in permutations:
                    perm = ''.join(perm)
                    result.add(perm)
    return result