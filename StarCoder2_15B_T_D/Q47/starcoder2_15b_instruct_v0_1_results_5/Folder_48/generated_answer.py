def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def palindromes_of_specific_lengths(s: str) -> set:
    palindromes = set()
    substring = s[155:284]
    for length in range(104, 121):
        for i in range(len(substring) - length + 1):
            window = substring[i:i + length]
            if is_palindrome(window) and window.isalpha():
                palindromes.add(window)
    return palindromes