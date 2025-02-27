from itertools import permutations

def palindromes_between_indices(s):
    char_count = {}
    for char in s[:6].lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    possible_palindromes = set()
    palindromes = generate_palindromes(char_count)
    for p in palindromes:
        if is_palindrome(p) and len(p) >= 6:
            possible_palindromes.add(p)
    return possible_palindromes

def generate_palindromes(char_count):
    first_half = [k * (v // 2) for k, v in char_count.items() if v > 1]
    mid = ''.join((k for k, v in char_count.items() if v % 2 == 1))
    perms = (''.join(p) for p in permutations(first_half))
    return set((p + mid + p[::-1] for p in perms))

def is_palindrome(s):
    return s == s[::-1]