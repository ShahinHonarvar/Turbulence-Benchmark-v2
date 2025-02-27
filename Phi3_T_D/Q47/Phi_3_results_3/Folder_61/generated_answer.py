def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]

    def find_palindromes(window):
        return {window[i:j] for i in range(len(window)) for j in range(i + 2, min(i + 31, len(window) + 1)) if is_palindrome(window[i:j]) and window[i:j].isalpha() and (20 <= len(window[i:j]) <= 30)}
    text = text.lower()
    return find_palindromes(text[:31])