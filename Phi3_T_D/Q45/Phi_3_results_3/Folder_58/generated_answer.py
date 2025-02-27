from itertools import permutations

def generate_palindromes(chars):
    half_length = len(chars) // 2
    if len(chars) % 2 == 0:
        first_half = chars[:half_length]
        middle = ''
    else:
        first_half = chars[:half_length + 1]
        middle = chars[half_length]
    char_combinations = set(first_half)
    palindromes = set()
    for perm in permutations(char_combinations, half_length):
        palindrome = ''.join(perm)
        palindrome = palindrome + middle + palindrome[::-1]
        palindromes.add(palindrome.lower())
    return palindromes

def palindromes_between_indices(s):
    index_1, index_2 = (0, 6)
    if index_2 <= index_1 or index_2 - index_1 < 5:
        return set()
    chars = ''.join(sorted(set(s[index_1:index_2 + 1].lower())))
    return generate_palindromes(chars)