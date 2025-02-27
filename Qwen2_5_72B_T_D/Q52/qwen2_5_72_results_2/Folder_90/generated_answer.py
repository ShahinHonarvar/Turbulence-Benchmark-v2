def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = ''.join(filter(str.isalpha, s))
    s = s.lower()
    n = 318
    result = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if is_palindrome(sub):
            result.add(sub)
    return result