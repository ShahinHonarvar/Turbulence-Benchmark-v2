import itertools

def palindromes_between_indices(string):
    letters = set(string.lower())
    palindromes = set()
    for combination in itertools.permutations(letters, 4):
        palindrome = ''.join(combination)
        if len(palindrome) >= 4 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes