from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[3:7]
    char_set = {c.lower() for c in sub_str if c.isalpha()}
    palindromes = set()
    for word_len in range(3, len(char_set) + 1):
        word_perms = [''.join(p) for p in permutations(char_set, word_len)]
        for word in word_perms:
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes