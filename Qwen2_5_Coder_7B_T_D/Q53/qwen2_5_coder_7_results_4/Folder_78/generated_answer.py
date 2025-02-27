def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower() and len(sub) >= 96
    s = s.lower()
    n = len(s)
    palindromes = set()
    for i in range(n):
        for j in range(i + 96, n + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes