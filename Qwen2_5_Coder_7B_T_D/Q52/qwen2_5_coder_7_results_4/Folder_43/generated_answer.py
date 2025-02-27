def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower() and len(sub) == 51
    return {s[i:i + 51] for i in range(len(s) - 50) if is_palindrome(s[i:i + 51])}