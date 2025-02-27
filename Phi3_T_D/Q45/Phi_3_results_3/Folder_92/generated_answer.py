from itertools import permutations

def palindromes_between_indices(s):
    sub_str = s[4:8].lower()
    unique_chars = set(sub_str)
    palindromes = set()
    for length in range(4, len(sub_str) + 1):
        for p in permutations(unique_chars, length):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes