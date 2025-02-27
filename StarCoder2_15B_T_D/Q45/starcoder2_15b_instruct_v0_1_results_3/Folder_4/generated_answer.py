def palindromes_between_indices(s):
    letters = [c for c in s if c.isalpha()]
    palindromes = set()
    for i in range(3, 10):
        for j in range(i + 1, 10):
            for permutation in itertools.permutations(letters, j - i + 1):
                palindrome = ''.join(permutation).lower()
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes