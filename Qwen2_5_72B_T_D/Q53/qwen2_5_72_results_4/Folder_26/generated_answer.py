def palindrome_of_length_at_least_n(s):
    s = ''.join(filter(str.isalpha, s)).lower()

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i + 31, n):
            if is_palindrome(s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return palindromes