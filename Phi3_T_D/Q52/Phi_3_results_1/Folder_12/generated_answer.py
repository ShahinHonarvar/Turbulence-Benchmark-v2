def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower() and sub.isalpha() and (len(sub) == 23)
    return {s[i:i + 23] for i in range(len(s) - 22) if is_palindrome(s[i:i + 23])}