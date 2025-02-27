def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(4, 10):
        for j in range(i + 1, 10):
            for permutation in itertools.permutations(letters[i:j]):
                palindrome = ''.join(permutation)
                if palindrome.lower() == palindrome[::-1].lower():
                    palindromes.add(palindrome)
    return palindromes