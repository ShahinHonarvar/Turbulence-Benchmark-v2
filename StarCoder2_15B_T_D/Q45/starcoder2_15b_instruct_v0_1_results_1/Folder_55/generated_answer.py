import itertools

def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for combination in itertools.combinations(letters, 3):
        palindrome = ''.join(combination)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes