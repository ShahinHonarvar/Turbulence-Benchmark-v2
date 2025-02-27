def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindromes_of_specific_lengths(s):
    start, end = (20, 74)
    min_length, max_length = (36, 42)
    palindromes = set()
    for length in range(min_length, max_length + 1):
        for i in range(start, end - length + 1):
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)) and is_palindrome(substring):
                palindromes.add(substring.lower())
    return palindromes