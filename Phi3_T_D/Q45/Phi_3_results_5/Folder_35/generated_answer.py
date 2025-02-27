import itertools

def palindromes_between_indices(s):
    sub_str = s[2:5]
    chars = [char.lower() for char in sub_str if char.isalpha()]
    all_combinations = set((''.join(p) for p in itertools.permutations(chars, len(chars))))
    palindromes = {sub for sub in all_combinations if len(sub) >= 4 and sub == sub[::-1]}
    return palindromes