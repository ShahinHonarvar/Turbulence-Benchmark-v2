from itertools import permutations

def generate_permutations(string):
    if len(string) <= 1:
        return [string]
    perm_list = []
    for i, char in enumerate(string):
        other_chars = string[:i] + string[i + 1:]
        for p in generate_permutations(other_chars):
            perm_list.append(char + p)
    return perm_list

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[0:9].lower()
    letter_set = {char for char in s if char.isalpha()}
    letters = ''.join(sorted(letter_set))
    valid_permutations = set()
    for perm in permutations(letters, 7):
        s = ''.join(perm)
        if is_palindrome(s):
            valid_permutations.add(s)
    return valid_permutations