def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 24, n):
            sub = s[i:j + 1]
            if is_palindrome(sub) and len(sub) >= 25:
                palindromes.add(sub)
    return palindromes