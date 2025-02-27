def is_palindrome(s):
    return s == s[::-1] and all((x.isalpha() for x in s))

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    n = 22
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + n, len(s) + 1):
            if is_palindrome(s[i:j]):
                palindromes.add(s[i:j])
    return palindromes