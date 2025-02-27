def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    result = set()
    n = 46
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring.isalpha() and is_palindrome(substring):
            result.add(substring)
    return result