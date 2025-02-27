def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(s):
    palindromes = set()
    s = s.lower()
    for i in range(len(s)):
        for j in range(i + 23, len(s) + 1):
            substring = s[i:j]
            if all((c.isalpha() for c in substring)) and all((c == c.lower() for c in substring)):
                if is_palindrome(substring):
                    palindromes.add(substring)
    return palindromes