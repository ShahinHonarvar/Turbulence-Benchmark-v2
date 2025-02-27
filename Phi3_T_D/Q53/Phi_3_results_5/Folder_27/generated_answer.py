import itertools

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    results = set()

    def is_palindrome(s):
        return s == s[::-1]
    for length in range(100, len(text)):
        for start in range(len(text) - length + 1):
            segment = text[start:start + length]
            if is_palindrome(segment):
                results.add(segment)
    return results