import string

def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def letter_only_substring(text, start, end):
    return ''.join((c for c in text[start:end + 1] if c.isalpha())).lower()

def palindromes_of_specific_lengths(text):
    if len(text) < 35:
        return set()
    palindromes_set = set()
    for i in range(35, 89):
        for length in range(24, 34):
            if i - length // 2 < 0 or i + length // 2 + 1 > len(text):
                continue
            candidate = text[i - length // 2:i + length // 2 + 1]
            if is_palindrome(candidate):
                palindromes_set.add(candidate.lower())
    return palindromes_set