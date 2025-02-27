def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    n = 13
    s = ''.join(filter(str.isalpha, s)).lower()
    palindromes = set()
    for length in range(n, len(s) + 1):
        for start in range(len(s) - length + 1):
            sub = s[start:start + length]
            if is_palindrome(sub):
                palindromes.add(sub)
    return palindromes