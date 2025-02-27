def palindrome_of_length_at_least_n(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    n = len(s)
    s = ''.join((char for char in s if char.isalpha())).lower()
    for length in range(56, n + 1):
        for i in range(n - length + 1):
            substring = s[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes