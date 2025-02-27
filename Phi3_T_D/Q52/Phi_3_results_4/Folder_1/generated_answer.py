def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_n(s):
    palindromes = set()
    for i in range(len(s) - 26):
        substring = s[i:i + 27]
        if all((c.isalpha() for c in substring)) and is_palindrome(substring.lower()):
            palindromes.add(substring)
    return palindromes