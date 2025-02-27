import itertools

def palindromes_between_indices(string):
    string = string.upper()
    letters = [c for c in string[2:9] if c.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters):
        palindrome = ''.join(permutation)
        if len(palindrome) >= 6 and palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes