def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    n = 188
    results = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring.isalpha() and is_palindrome(substring):
            results.add(substring)
    return results