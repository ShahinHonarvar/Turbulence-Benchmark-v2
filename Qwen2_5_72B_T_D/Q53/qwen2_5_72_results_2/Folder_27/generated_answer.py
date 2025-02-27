def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def is_palindrome(sub):
        return sub == sub[::-1]
    result = set()
    for i in range(len(s)):
        for j in range(i + 100, len(s) + 1):
            if is_palindrome(s[i:j]):
                result.add(s[i:j])
    return result