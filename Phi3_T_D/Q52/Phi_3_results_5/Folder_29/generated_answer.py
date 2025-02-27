def palindrome_of_length_n(s):

    def is_palindrome(subs):
        return subs == subs[::-1]
    return {s[i:i + 19].lower() for i in range(len(s) - 18) if is_palindrome(s[i:i + 19]) and s[i:i + 19].isalpha()}