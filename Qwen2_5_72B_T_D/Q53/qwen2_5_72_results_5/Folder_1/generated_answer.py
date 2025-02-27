def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)

    def is_palindrome(x):
        return x == x[::-1]
    result = set()
    for i in range(n):
        for j in range(i + 28, n):
            if is_palindrome(s[i:j + 1]):
                result.add(s[i:j + 1])
    return result