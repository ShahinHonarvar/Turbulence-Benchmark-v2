def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def valid_combinations(text):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    chars = {}
    for char in text[3:10]:
        if char.lower() in alphabet:
            chars[char.lower()] = chars.get(char.lower(), 0) + 1
    return chars

def palindromes_between_indices(text):
    valid_chars = valid_combinations(text)
    candidates = []

    def generate_palindromes(half, counts):
        if len(half) == 5:
            if is_palindrome(half):
                candidates.append(half.lower())
            return
        for char in sorted(counts.keys()):
            if counts[char] > 0 and half.count(char) // 2 < valid_chars[char] // 2:
                counts_new = counts.copy()
                counts_new[char] -= 1
                generate_palindromes(half + char, counts_new)
    generate_palindromes('', valid_chars)
    return set(candidates)