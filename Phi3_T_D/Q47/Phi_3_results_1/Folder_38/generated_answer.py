import re

def palindromes_of_specific_lengths(text):

    def is_english_letter(c):
        return c.isalpha() and c.isascii()

    def is_case_insensitive_palindrome(s):
        return s.lower() == s[::-1].lower()
    sub_text = text[18:88]
    result = set()
    for length in range(38, 61):
        for i in range(0, len(sub_text) - length + 1):
            candidate = sub_text[i:i + length]
            if all((is_english_letter(c) for c in candidate)):
                if is_case_insensitive_palindrome(candidate):
                    result.add(candidate)
    return result