def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1] and sub.isalpha()
    s = s.lower()
    result = set()
    for i in range(len(s) - 400):
        substring = s[i:i + 401]
        if is_palindrome(substring):
            result.add(substring)
    return result