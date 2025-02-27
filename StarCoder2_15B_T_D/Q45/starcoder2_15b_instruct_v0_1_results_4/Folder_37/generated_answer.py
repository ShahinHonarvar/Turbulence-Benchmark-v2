import itertools

def palindromes_between_indices(string):
    letters = [letter for letter in string.lower() if letter.isalpha()]
    palindromes = set()
    for combination in itertools.permutations(letters, 5):
        word = ''.join(combination)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes