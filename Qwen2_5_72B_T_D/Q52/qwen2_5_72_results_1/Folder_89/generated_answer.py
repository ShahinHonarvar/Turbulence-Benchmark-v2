def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = ''.join(filter(str.isalpha, s)).lower()
    n = 37
    result = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if is_palindrome(sub):
            result.add(sub)
    return result