def palindrome_of_length_at_least_n(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    text_lower = text.lower()
    result_set = set()

    def is_palindrome(s):
        return s == s[::-1]
    for i in range(len(text)):
        for j in range(i + 147, len(text) + 1):
            substring = text_lower[i:j]
            if all((char in alphabet for char in substring)) and is_palindrome(substring):
                result_set.add(substring)
    return result_set