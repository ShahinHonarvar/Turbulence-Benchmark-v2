def is_palindrome(s):
    return s.lower() == s.lower()[::-1].replace(' ', '')

def palindromes_of_specific_lengths(text):
    result = set()
    for length in range(20, 67):
        for start in range(15, 96 - length + 1):
            substring = text[start:start + length]
            if all((char.isalpha() for char in substring)) and is_palindrome(substring):
                result.add(substring)
    return result