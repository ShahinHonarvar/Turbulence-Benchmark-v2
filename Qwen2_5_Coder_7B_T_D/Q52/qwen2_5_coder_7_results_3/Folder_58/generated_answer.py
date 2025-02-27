def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    n = 223
    result = set()
    for i in range(len(s) - n + 1):
        sub = s[i:i + n]
        if is_palindrome(sub) and sub.isalpha():
            result.add(sub)
    return result