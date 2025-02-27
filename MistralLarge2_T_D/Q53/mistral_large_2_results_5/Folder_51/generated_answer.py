def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    result = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 63, n + 1):
            sub = s[i:j]
            if sub.isalpha() and is_palindrome(sub):
                result.add(sub)
    return result