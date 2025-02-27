def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    s = s.lower()
    substring_length = 6
    return {s[i:i + substring_length] for i in range(len(s) - substring_length + 1) if s[i:i + substring_length].isalpha() and all((ch.isalpha() for ch in s[i:i + substring_length])) and is_palindrome(s[i:i + substring_length])}