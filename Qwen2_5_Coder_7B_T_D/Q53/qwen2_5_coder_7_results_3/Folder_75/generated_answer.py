def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower() and len(sub) >= 40
    s = ''.join(filter(str.isalpha, s))
    palindromes = set()
    n = len(s)
    for i in range(n):
        for j in range(i, n):
            if is_palindrome(s[i:j + 1]):
                palindromes.add(s[i:j + 1])
    return palindromes