from itertools import permutations

def palindromes_between_indices(s):
    eng_letters = set('abcdefghijklmnopqrstuvwxyz')
    s = s[:3].lower()
    found_chars = {c for c in s if c.isalpha()}
    if len(found_chars) < 3 or found_chars - eng_letters:
        return set()
    lookup = {c: f'{c}{c}' for c in 'abcdefghijklmnopqrstuvwxyz'}
    palindromes = set()
    for p in permutations(found_chars):
        word = ''.join(p)
        for key, value in lookup.items():
            word = word.replace(key, value)
        palindromes.add(word)
    return palindromes