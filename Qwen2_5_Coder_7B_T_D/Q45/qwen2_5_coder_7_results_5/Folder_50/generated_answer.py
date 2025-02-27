def palindromes_between_indices(s):
    s = s[4:9].lower()
    letters = set(s)
    result = set()
    for length in range(5, len(letters) + 1):
        for combination in combinations(letters, length):
            for perm in permutations(combination):
                palindrome = ''.join(perm) + ''.join(perm[::-1][1:])
                if len(palindrome) == length * 2 - 1:
                    result.add(palindrome)
    return result