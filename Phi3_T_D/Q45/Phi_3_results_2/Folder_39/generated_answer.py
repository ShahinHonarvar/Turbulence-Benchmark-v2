from itertools import combinations, permutations
    from collections import Counter

def palindromes_between_indices(s):

    def is_palindrome(s):
        return s == s[::-1]
    target_str = s[2:6].lower()
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    target_counter = Counter(target_str)
    valid = all((target_counter[c] >= Counter(english_letters)[c] for c in english_letters))
    if valid:
        l = len(target_str)
        palindromes = set()
        for palindrome_length in range(3, l + 1):
            if palindrome_length % 2 == 0:
                half_length = palindrome_length // 2
                for first_half in permutations(target_str, half_length):
                    if is_palindrome(''.join(first_half) + ''.join(first_half[::-1])):
                        palindromes.add(''.join(first_half) + ''.join(first_half[::-1]))
            else:
                for center in target_str:
                    for first_half in permutations(target_str.replace(center, ''), (palindrome_length - 1) // 2):
                        palindromes.add(''.join(first_half) + center + ''.join(first_half[-1::-1]))
        return palindromes
    else:
        return set()