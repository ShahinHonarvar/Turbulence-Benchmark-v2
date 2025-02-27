def palindromes_between_indices(s):
    letters = set(s[4:10].lower())
    palindromes = set()
    for length in range(3, len(letters) + 1):
        for combination in combinations(letters, length):
            for perm in permutations(combination):
                palindrome = ''.join(perm)
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes