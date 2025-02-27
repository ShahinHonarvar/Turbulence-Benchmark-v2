def is_english_letter(char):
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z'

def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindromes_of_specific_lengths(s):
    start, end = (27, 77)
    min_length, max_length = (18, 19)
    substrings = set()
    for length in range(min_length, max_length + 1):
        for i in range(start, end - length + 1):
            candidate = s[i:i + length]
            if all((is_english_letter(ch) for ch in candidate)) and is_palindrome(candidate):
                substrings.add(candidate)
    return substrings