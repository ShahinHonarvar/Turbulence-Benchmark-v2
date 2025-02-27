def is_palindrome(s):
    return s == s[::-1]

def find_palindromes_at_least_n(s, n):
    s = s.lower()
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n // 2, len(s)):
            if j - i + 1 >= n and is_palindrome(s[i:j + 1]):
                palindromes.add(s[i:j + 1].capitalize())
    return palindromes

def palindrome_of_length_at_least_n(s):
    return find_palindromes_at_least_n(s, 42)