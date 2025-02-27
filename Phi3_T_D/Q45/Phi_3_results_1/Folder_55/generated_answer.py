from itertools import permutations

def palindromes_between_indices(s):
    english_letters_set = set('abcdefghijklmnopqrstuvwxyz')

    def is_palindrome(word):
        return word == word[::-1]
    start_end_chars = set(s[0:3].lower()) & english_letters_set
    if len(start_end_chars) < 2:
        return set()
    palindromes = set()
    for c1 in start_end_chars:
        for c2 in start_end_chars:
            if c1 != c2:
                permutation_set = {''.join(p) for p in permutations([c1, c2, c1], 3)}
                for p in permutation_set:
                    if is_palindrome(p):
                        palindromes.add(p)
    return palindromes