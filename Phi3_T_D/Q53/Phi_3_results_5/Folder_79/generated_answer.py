def palindrome_of_length_at_least_n(text):

    def is_palindrome(s):
        return s == s[::-1]
    text_lower = text.lower()
    found_palindromes = set()
    for start in range(len(text_lower)):
        for end in range(start + 17, len(text_lower) + 1):
            candidate = text_lower[start:end]
            if is_palindrome(candidate):
                found_palindromes.add(candidate)
    return found_palindromes