def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(3, 10):
        for j in range(i, 10):
            for permutation in itertools.permutations(letters, j - i + 1):
                palindrome = ''.join(permutation).lower()
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes