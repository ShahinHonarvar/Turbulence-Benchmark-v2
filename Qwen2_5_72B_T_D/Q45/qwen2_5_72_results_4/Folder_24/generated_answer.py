from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substring = s[2:10]
    char_count = {}
    for char in substring:
        if char.isalpha():
            char_count[char.lower()] = char_count.get(char.lower(), 0) + 1
    half_palindrome = ''
    for char, count in char_count.items():
        half_palindrome += char * (count // 2)
    half_permutations = set(permutations(half_palindrome))
    palindromes = set()
    for half in half_permutations:
        half_str = ''.join(half)
        for odd_char in [char for char, count in char_count.items() if count % 2 != 0] + ['']:
            palindrome = half_str + odd_char + half_str[::-1]
            if len(palindrome) >= 4:
                palindromes.add(palindrome)
    return palindromes