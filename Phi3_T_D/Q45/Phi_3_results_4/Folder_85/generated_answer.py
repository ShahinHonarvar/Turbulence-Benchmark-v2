from itertools import permutations

def is_palindrome(s):
    return s == s[::-1]

def palindromes_between_indices(s):
    s = s[2:8]
    half_len = 7 // 2
    possible_chars = ''.join(sorted(set(s.lower())))[:half_len]
    palindromes = set()

    def build_palindrome(chars, start='', middle=''):
        if len(start) == half_len:
            full_palindrome = start + middle + start[::-1]
            if is_palindrome(full_palindrome):
                palindromes.add(full_palindrome)
            return
        for char in chars:
            if not start or char >= start[-1]:
                build_palindrome(chars, start + char, middle)
                if len(start) < half_len:
                    build_palindrome(chars, start, char)
    build_palindrome(possible_chars)
    return palindromes