def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 41

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindrome_set = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            sub = s[i:j]
            if is_palindrome(sub):
                palindrome_set.add(sub)
    return palindrome_set