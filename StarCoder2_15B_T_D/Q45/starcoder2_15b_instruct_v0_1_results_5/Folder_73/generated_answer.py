import itertools

def palindromes_between_indices(string):
    letters = [char for char in string if char.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters[3:7], 3):
        palindrome = ''.join(permutation).lower()
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes