def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    palindromes = set()
    n = 141
    while n <= len(s):
        for i in range(len(s) - n + 1):
            substring = s[i:i + n]
            if all((c.isalpha() for c in substring)) and is_palindrome(substring):
                palindromes.add(substring)
        n += 1
    return palindromes