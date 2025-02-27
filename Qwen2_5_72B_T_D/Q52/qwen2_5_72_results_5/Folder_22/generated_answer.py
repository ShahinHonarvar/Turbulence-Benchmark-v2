def palindrome_of_length_n(s):

    def is_palindrome(t):
        return t.lower() == t.lower()[::-1]
    length = 20
    s = ''.join(filter(str.isalpha, s))
    result = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if is_palindrome(substring):
            result.add(substring)
    return result