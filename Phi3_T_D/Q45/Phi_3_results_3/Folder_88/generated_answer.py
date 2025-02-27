from collections import Counter
    from itertools import permutations

def is_palindrome(candidate):
    return candidate.lower() == candidate.lower()[::-1]

def palindromes_between_indices(s):
    substr = s[3:8]
    char_counter = Counter(substr.lower())
    english_letters_set = set('abcdefghijklmnopqrstuvwxyz')
    possible_chars = ''.join([char * count for char, count in char_counter.items() if char in english_letters_set])
    max_perms = len(possible_chars) // 8
    palindromes = set()
    for perm_len in range(6, len(possible_chars) + 1):
        for perm in permutations(possible_chars, perm_len // 2):
            if perm_len % 2 == 0:
                center_char = ''
                half_pal = perm
            else:
                center_char = possible_chars[perm_len // 2 % len(possible_chars)]
                half_pal = perm[:perm_len // 2]
            candidate = ''.join(half_pal) + center_char + ''.join(reversed(half_pal))
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes