def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(3, 9):
        for j in range(i + 1, 9):
            for permutation in itertools.permutations(letters[i:j]):
                palindrome = ''.join(permutation)
                if palindrome.lower() == palindrome.lower()[::-1] and len(palindrome) >= 4:
                    palindromes.add(palindrome)
    return palindromes