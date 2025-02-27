def is_palindrome(s):
    return s == s[::-1]

def find_palindromes_at(center, s, left, right, results):
    while left >= 0 and right < len(s) and is_palindrome(s[left:right + 1].lower()):
        results.add(s[left:right + 1])
        left -= 1
        right += 1

def palindrome_of_length_at_least_n(s):
    results = set()
    n = 49
    for i in range(len(s)):
        find_palindromes_at(i, s, i - 1, i, results)
        find_palindromes_at(i, s, i - 1, i + 1, results)
    return {p for p in results if len(p) >= n and p.isalpha()}