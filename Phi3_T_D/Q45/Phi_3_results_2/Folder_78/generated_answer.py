from itertools import permutations

def palindromes_between_indices(s):
    substring = s[6:10]
    char_count = {}
    for char in substring.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    odd_char = ''
    even_chars = ''
    for char, count in char_count.items():
        if count % 2 == 1:
            if odd_char:
                return set()
            odd_char = char
        even_chars += char * (count // 2)
    center = odd_char * (char_count[odd_char] - 1 if odd_char else '') + odd_char * (1 if odd_char else '')
    half_length = len(substring) // 2
    half_palindromes = [''.join(p) for p in permutations(even_chars, half_length)]
    palindromes = set()
    for half in half_palindromes:
        palindromes.add(half + center + half[::-1])
    return palindromes