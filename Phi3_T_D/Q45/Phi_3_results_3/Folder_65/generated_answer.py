from itertools import permutations

def palindromes_between_indices(input_string):
    substring = input_string[:7].lower()
    letters = ''.join(filter(str.isalpha, substring))
    if len(letters) < 5:
        return set()
    all_perms = set(permutations(letters, 5))
    palindromes = set((''.join(p) for p in all_perms if ''.join(p) == ''.join(p)[::-1]))
    return palindromes