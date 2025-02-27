def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = ''.join(filter(str.isalpha, s))
    n = 100
    length = len(s)
    result = set()
    for i in range(length - n + 1):
        sub = s[i:i + n]
        if is_palindrome(sub):
            result.add(sub)
    return result