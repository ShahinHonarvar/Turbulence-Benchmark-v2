def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    length = len(s)
    result = set()
    for i in range(length):
        for j in range(i + 15, length + 1):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring.lower()):
                result.add(substring.lower())
    return result