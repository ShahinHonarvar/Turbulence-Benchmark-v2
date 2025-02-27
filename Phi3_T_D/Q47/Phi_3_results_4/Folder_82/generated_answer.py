def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def is_alpha(s: str) -> bool:
    return s.isalpha()

def palindromes_of_specific_lengths(s: str) -> set:
    substring = s[3:301]
    palindromes = set()
    for length in range(30, 301):
        for i in range(301 - length):
            substring_candidate = substring[i:i + length]
            if is_palindrome(substring_candidate) and all((is_alpha(char) for char in substring_candidate)):
                palindromes.add(substring_candidate.lower())
    return palindromes