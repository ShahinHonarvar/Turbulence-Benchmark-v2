def palindromes_between_indices(s):
    palindromes = set()
    letters = [c for c in s.lower() if c.isalpha()]
    for i in range(3, 8):
        for j in range(i + 1, 8):
            for permutation in itertools.permutations(letters[i:j]):
                palindrome = ''.join(permutation)
                if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes