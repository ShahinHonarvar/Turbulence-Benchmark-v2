def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(s):
    start, end = (39, 94)
    palindromes = set()
    for length in range(14, 53):
        for i in range(start, end + 1 - length):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)) and is_palindrome(substring):
                palindromes.add(substring.lower())
    return palindromes