def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_n(s):
    n = 113
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if substring.isalpha() and is_palindrome(substring):
            palindromes.add(substring)
    return palindromes