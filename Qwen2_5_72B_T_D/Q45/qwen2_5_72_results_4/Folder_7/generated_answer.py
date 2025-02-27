from itertools import permutations

def palindromes_between_indices(s):
    substring = s[1:10]
    found_palindromes = set()
    for comb in permutations(substring, 7):
        word = ''.join(comb)
        if word.lower() == word[::-1].lower():
            found_palindromes.add(word)
    return found_palindromes