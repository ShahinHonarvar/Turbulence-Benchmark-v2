def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]

def palindromes_of_specific_lengths(text):
    palindromes = set()
    for length in range(12, 221):
        for i in range(12, len(text) - length + 12):
            substring = text[i:i + length]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring)
    return palindromes