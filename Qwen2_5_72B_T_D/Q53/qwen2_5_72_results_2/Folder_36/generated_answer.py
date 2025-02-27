def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = ''.join(filter(str.isalpha, s))
    n = len(s)
    result = set()
    for i in range(n):
        for j in range(i + 139, n + 1):
            if is_palindrome(s[i:j]):
                result.add(s[i:j])
    return result