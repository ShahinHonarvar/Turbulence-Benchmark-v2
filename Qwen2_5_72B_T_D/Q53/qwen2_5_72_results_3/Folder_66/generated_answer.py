def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    n = len(s)
    result = set()
    for i in range(n):
        for j in range(i + 75, n):
            if is_palindrome(s[i:j + 1]):
                result.add(s[i:j + 1])
    return result