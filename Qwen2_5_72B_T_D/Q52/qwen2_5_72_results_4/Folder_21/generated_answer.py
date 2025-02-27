def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    length = 407
    result = set()
    for i in range(len(s) - length + 1):
        substring = s[i:i + length]
        if substring.isalpha() and is_palindrome(substring):
            result.add(substring)
    return result