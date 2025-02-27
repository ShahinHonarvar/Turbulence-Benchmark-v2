import itertools

def palindromes_between_indices(string):
    letters = [letter for letter in string.lower() if letter.isalpha()]
    palindromes = set()
    for combination in itertools.permutations(letters, 3):
        palindrome = ''.join(combination)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes