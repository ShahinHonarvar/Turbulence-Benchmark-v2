def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]

    def valid_palindromes():
        for i in range(len(s) - 34):
            substring = s[i:i + 34].lower()
            if all((char.isalpha() for char in substring)):
                yield substring
    return {sub for sub in valid_palindromes() if is_palindrome(sub)}