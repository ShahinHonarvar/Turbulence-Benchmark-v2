from itertools import permutations

def palindromes_between_indices(s):
    substr = s[:7].lower()
    alphabet_set = set('abcdefghijklmnopqrstuvwxyz')
    potential_chars = set(substr) & alphabet_set
    if len(potential_chars) < 4:
        return set()

    def is_palindrome(word):
        return word == word[::-1]
    palindromes = set()
    for p in permutations(potential_chars, 4):
        p_string = ''.join(p)
        if is_palindrome(p_string):
            palindromes.add(p_string)
    return palindromes