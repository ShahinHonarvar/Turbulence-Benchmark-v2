def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(2, 10):
        for j in range(i + 1, 10):
            for permutation in itertools.permutations(letters, j - i + 1):
                palindrome = ''.join(permutation).lower()
                if palindrome == palindrome[::-1] and len(palindrome) >= 6:
                    palindromes.add(palindrome)
    return palindromes