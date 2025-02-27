def palindrome_of_length_at_least_n(s):
    s = s.lower()

    def is_palindrome(sub):
        return sub == sub[::-1]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 44, len(s)):
            substring = s[i:j + 1]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes