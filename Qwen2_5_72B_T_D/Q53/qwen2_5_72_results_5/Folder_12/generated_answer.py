def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    length = len(s)
    result = set()
    for i in range(length):
        for j in range(i + 50, length):
            if is_palindrome(s[i:j + 1]):
                result.add(s[i:j + 1])
    return result