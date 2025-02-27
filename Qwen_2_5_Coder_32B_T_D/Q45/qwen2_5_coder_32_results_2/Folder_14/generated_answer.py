import itertools

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[4:6].lower()))
    perms = set(itertools.permutations(letters, len(letters)))
    palindromes = set()
    for perm in perms:
        word = ''.join(perm)
        if len(word) >= 3 and word == word[::-1]:
            palindromes.add(word)
    return palindromes