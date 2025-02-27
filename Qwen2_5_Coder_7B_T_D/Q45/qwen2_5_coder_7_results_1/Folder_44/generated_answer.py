def palindromes_between_indices(s):
    letters = s[2:8]
    lower_letters = letters.lower()
    unique_letters = set(lower_letters)
    result = set()
    for length in range(3, len(unique_letters) + 1):
        for combination in itertools.combinations(unique_letters, length):
            for perm in itertools.permutations(combination):
                palindrome = ''.join(perm) + ''.join(perm[::-1][1:])
                if len(palindrome) == length * 2 - 1:
                    result.add(palindrome)
    return result