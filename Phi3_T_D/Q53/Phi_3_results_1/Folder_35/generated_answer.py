from collections import Counter

def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    valid_char_count = Counter((ch for ch in text if ch.isalpha()))
    valid_chars = ''.join(valid_char_count.keys())
    n = 26
    palindromes = set()
    for char in valid_chars:
        for _ in range(valid_char_count[char] - n + 1):
            start_len = 2 * n - valid_char_count[char]
            for i in range(len(text) - start_len + 1):
                for j in range(start_len):
                    if text[i + j] not in valid_chars:
                        break
                else:
                    candidate_palindrome = text[i:i + start_len]
                    if is_palindrome(candidate_palindrome):
                        palindromes.add(candidate_palindrome)
    return palindromes