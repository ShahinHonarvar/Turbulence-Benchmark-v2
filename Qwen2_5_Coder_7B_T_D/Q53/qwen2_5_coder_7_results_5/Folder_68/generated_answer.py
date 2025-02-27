def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    result = set()
    s = s.lower()
    length = len(s)
    for i in range(length):
        for j in range(i + 21, length + 1):
            sub = s[i:j]
            if is_palindrome(sub):
                result.add(sub)
    return result