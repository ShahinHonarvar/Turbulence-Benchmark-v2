import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:9])).lower()
    p = set()
    for combination in itertools.permutations(letters, 6):
        word = ''.join(combination)
        if word == word[::-1]:
            p.add(word)
    return p