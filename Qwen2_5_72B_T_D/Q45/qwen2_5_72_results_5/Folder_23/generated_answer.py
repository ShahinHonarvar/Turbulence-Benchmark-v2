from itertools import permutations

def palindromes_between_indices(s):
    substring = s[:7].lower()
    char_list = [char for char in substring if char.isalpha()]
    palindromes = set()
    for perm in permutations(char_list, 4):
        word = ''.join(perm)
        if word == word[::-1]:
            palindromes.add(word)
    return palindromes