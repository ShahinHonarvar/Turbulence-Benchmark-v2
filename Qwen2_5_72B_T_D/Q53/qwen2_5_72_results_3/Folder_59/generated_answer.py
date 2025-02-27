def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = len(s)
    min_length = 20
    palindrome_set = set()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(n):
        for j in range(i + min_length, n + 1):
            substring = s[i:j]
            if is_palindrome(substring):
                palindrome_set.add(substring)
    return palindrome_set