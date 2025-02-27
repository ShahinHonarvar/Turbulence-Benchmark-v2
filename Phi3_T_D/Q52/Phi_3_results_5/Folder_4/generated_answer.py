def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_n(s):
    s = s.lower()
    palindromes = set()
    for i in range(len(s) - 14):
        substring = s[i:i + 15]
        if is_palindrome(substring):
            palindromes.add(substring)
    return palindromes