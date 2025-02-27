def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(2, 7):
        for j in range(i + 1, 7):
            for permutation in combinations(letters, j - i + 1):
                palindrome = ''.join(permutation).lower()
                if palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes