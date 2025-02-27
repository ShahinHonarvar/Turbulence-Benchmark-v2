def palindrome_of_length_at_least_n(s):

    def is_palindrome(string):
        return string == string[::-1]
    s = s.lower()
    min_length = 78
    unique_chars = 'abcdefghijklmnopqrstuvwxyz'
    found_palindromes = set()
    for start in range(len(s)):
        for end in range(start + min_length, len(s) + 1):
            substr = s[start:end]
            if all((char in unique_chars for char in substr)) and is_palindrome(substr):
                found_palindromes.add(substr)
    return found_palindromes