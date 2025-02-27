def palindrome_of_length_at_least_n(s):
    n = 86
    palindromes = set()
    s = s.lower()

    def is_palindrome(sub):
        return sub == sub[::-1]
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes