def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    result = set()
    n = 188
    for i in range(len(s) - n + 1):
        sub = ''.join(filter(str.isalpha, s[i:i + n]))
        if len(sub) == n and is_palindrome(sub):
            result.add(sub)
    return result