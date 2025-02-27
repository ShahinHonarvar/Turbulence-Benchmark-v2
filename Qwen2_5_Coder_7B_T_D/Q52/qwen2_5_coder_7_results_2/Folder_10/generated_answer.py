def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    n = 54
    result = set()
    for i in range(len(s) - n + 1):
        substr = s[i:i + n]
        if is_palindrome(substr):
            result.add(substr)
    return result