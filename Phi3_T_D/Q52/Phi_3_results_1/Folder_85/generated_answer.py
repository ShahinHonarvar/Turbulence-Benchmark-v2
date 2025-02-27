def palindrome_of_length_n(s):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    for i in range(len(s) - 45):
        substring = s[i:i + 46].lower()
        if all((c.isalpha() for c in substring)) and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes