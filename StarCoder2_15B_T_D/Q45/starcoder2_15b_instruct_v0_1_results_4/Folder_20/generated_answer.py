def palindromes_between_indices(string):
    characters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(2, 9):
        for j in range(i + 1, 9):
            for permutation in itertools.permutations(characters, j - i + 1):
                palindrome = ''.join(permutation).lower()
                if palindrome == palindrome[::-1] and len(palindrome) >= 4:
                    palindromes.add(palindrome)
    return palindromes