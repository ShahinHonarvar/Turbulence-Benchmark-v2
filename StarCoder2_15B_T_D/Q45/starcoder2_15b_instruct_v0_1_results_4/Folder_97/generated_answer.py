import itertools

def palindromes_between_indices(string):
    letters = [letter for letter in string if letter.isalpha()]
    palindromes = set()
    for permutation in itertools.permutations(letters, 3):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes