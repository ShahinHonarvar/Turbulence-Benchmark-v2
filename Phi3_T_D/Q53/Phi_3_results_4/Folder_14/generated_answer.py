def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    results = set()
    text_lower = text.lower()
    for i in range(len(text)):
        for j in range(i + 13, len(text) + 1):
            substring = text_lower[i:j]
            if all((c.isalpha() for c in substring)) and is_palindrome(substring):
                results.add(substring)
    return results