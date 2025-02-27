def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(s):
    start, end = (44, 99)
    palindromes = set()
    s = s[start:end + 1].lower()
    for length in range(13, 43):
        for i in range(len(s) - length + 1):
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes