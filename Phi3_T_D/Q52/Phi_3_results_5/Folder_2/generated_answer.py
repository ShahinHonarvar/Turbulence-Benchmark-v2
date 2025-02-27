def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring == substring[::-1]

    def get_substrings_of_length_n(s, n):
        return [s[i:i + n] for i in range(len(s) - n + 1)]
    length = 147
    s = s.lower()
    substrings = get_substrings_of_length_n(s, length)
    return {substring for substring in substrings if is_palindrome(substring)}