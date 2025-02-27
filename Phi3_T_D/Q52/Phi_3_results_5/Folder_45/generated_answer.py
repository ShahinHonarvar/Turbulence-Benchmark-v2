def palindrome_of_length_n(s):

    def is_palindrome(substring):
        return substring == substring[::-1]
    return {s[i:j + 1].lower() for i in range(len(s)) for j in range(i + 20, len(s)) if is_palindrome(s[i:j + 1])}