def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    result = set()
    for i in range(len(s) - 62):
        substring = s[i:i + 63]
        if substring.isalpha() and is_palindrome(substring):
            result.add(substring)
    return result