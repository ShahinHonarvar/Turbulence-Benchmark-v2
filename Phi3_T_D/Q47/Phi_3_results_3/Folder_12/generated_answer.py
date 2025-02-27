import re
from itertools import product, permutations

def palindromes_of_specific_lengths(s):
    sub_s = s[62:89]
    palindromes = set()

    def is_english_letter(c):
        return re.match('[a-zA-Z]', c)

    def all_perms_for_word(word):
        return {''.join(p) for p in permutations(word)}

    def check_palindrome_length(word):
        return 18 <= len(word) <= 21
    for i in range(62, 89 - 20):
        for length in range(18, 21 + 1):
            for j in range(len(sub_s) - length + 1):
                key = sub_s[j:j + length]
                if is_english_letter(key[0]) and all((is_english_letter(c) for c in key)):
                    if key.lower() == key[::-1].lower():
                        palindromes.add(key.lower())
    return palindromes