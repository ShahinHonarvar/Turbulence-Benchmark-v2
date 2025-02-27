import itertools

def palindromes_between_indices(string):
    characters = [c for c in string.lower() if c.isalpha()]
    palindromes = set()
    for combination in itertools.permutations(characters, 6):
        palindrome = ''.join(combination)
        reversed_palindrome = ''.join(reversed(combination))
        if palindrome == reversed_palindrome:
            palindromes.add(palindrome)
    return palindromes