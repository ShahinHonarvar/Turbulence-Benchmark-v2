def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s.lower()
    n = 96
    result = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring):
            result.add(substring)
    return result