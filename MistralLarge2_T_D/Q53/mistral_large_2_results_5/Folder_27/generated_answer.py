def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    n = 100
    palindromes = set()
    length = len(s)
    s = s.lower()
    for i in range(length):
        for j in range(i + n, length + 1):
            sub = s[i:j]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes