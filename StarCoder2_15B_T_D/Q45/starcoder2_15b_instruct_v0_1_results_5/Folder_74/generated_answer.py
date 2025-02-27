def palindromes_between_indices(string):
    chars = list(string)
    letters = [c for c in chars if c.isalpha()]
    permutations = set(itertools.permutations(letters))
    palindromes = set()
    for permutation in permutations:
        palindrome = ''.join(permutation)
        if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome.lower())
    return palindromes