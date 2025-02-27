from collections import defaultdict

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    max_length = 74

    def is_palindrome(s):
        return s == s[::-1]

    def all_substrings(text):
        length = len(text)
        return {text[i:j] for i in range(length) for j in range(i + 1, length + 1)}

    def filter_palindromes(substrings):
        return {s for s in substrings if is_palindrome(s) and len(s) >= max_length and s.isalpha()}
    all_subs = all_substrings(text)
    return filter_palindromes(all_subs)