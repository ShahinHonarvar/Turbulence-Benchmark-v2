def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    s = s.lower()
    n = 98
    result = set()
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            sub = s[i:j]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub)
    return result