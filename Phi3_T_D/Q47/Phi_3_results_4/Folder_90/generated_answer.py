def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def palindromes_of_specific_lengths(text: str) -> set:
    result = set()
    start, end = (106, 280)
    for length in range(136, 152):
        for i in range(start, end - length + 2):
            substring = text[i:i + length]
            if all((c.isalpha() for c in substring)) and is_palindrome(substring.lower()):
                result.add(substring.lower())
    return result