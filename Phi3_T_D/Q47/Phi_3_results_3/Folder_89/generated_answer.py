def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def palindromes_of_specific_lengths(s: str) -> set:
    target_range = s[18:89]
    valid_palindromes = set()
    for length in range(12, 15):
        for i in range(len(target_range) - length + 1):
            candidate = target_range[i:i + length].lower()
            if candidate.isalpha() and is_palindrome(candidate):
                valid_palindromes.add(candidate)
    return valid_palindromes