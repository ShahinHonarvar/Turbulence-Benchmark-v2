def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s.lower()
    result = set()
    n = 83
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            if is_palindrome(s[i:j]):
                result.add(s[i:j])
    return result