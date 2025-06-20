def palindrome_of_length_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    n = 318
    result = set()
    for i in range(len(s) - n + 1):
        if is_palindrome(s[i:i + n]):
            result.add(s[i:i + n])
    return result