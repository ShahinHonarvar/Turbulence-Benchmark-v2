def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    length = 85
    s = ''.join(filter(str.isalpha, s))
    return {s[i:i + length] for i in range(len(s) - length + 1) if is_palindrome(s[i:i + length])}