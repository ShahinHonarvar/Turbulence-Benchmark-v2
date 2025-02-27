def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    palindromes = set()
    for i in range(2, 9):
        for j in range(i + 1, 9):
            for permutation in itertools.permutations(letters[i:j]):
                palindrome = ''.join(permutation)
                if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
                    palindromes.add(palindrome)
    return palindromes