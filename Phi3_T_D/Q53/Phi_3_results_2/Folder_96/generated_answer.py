def palindrome_of_length_at_least_n(s):
    s = s.lower()
    length = len(s)
    result = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(length):
        for j in range(i + 23, length + 1):
            if is_palindrome(s[i:j]):
                result.add(s[i:j])
    return result