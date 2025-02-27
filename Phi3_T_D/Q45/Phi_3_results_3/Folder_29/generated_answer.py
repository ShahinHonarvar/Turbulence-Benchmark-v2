from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:10].lower()
    char_counts = {}
    for char in s:
        if char.isalpha():
            char_counts[char] = char_counts.get(char, 0) + 1
    return {''.join(half)[::-1] for half in permutations(''.join((char * count for char, count in char_counts.items())), 3) if len(half) == 6}