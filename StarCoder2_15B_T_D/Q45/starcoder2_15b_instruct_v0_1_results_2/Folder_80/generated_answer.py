import itertools

def palindromes_between_indices(string):
    letters = [c for c in string if c.isalpha()]
    combinations = itertools.combinations(letters, 7)
    palindromes = set()
    for combination in combinations:
        palindrome = ''.join(combination)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes