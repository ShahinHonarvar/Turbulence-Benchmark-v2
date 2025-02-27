def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = ''.join(filter(str.isalpha, s))
    result = set()
    n = 59
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            sub = s[i:j]
            if is_palindrome(sub):
                result.add(sub)
    return result