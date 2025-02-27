def palindromes_between_indices(s):
    substring = s[5:8].lower()
    letters = set(substring)
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combination in itertools.combinations(letters, length):
            for perm in itertools.permutations(combination):
                palindrome = ''.join(perm)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes