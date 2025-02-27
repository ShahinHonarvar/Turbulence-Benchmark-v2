def is_palindrome(s):
    return s == s[::-1]

def check_letter_only(s):
    return s.isalpha()

def palindromes_of_specific_lengths(s):
    result = set()
    for length in range(42, 78):
        for i in range(12, 93 - length + 1):
            substring = s[i:i + length].lower()
            if is_palindrome(substring) and check_letter_only(substring):
                result.add(substring)
    return result