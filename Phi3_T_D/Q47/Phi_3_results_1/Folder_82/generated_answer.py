def is_palindrome(s: str) -> bool:
    return s == s[::-1]

def palindromes_of_specific_lengths(input_string: str) -> set:
    result = set()
    substring = input_string[3:301]
    for length in range(30, 301):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length].lower()
            if candidate.isalpha() and is_palindrome(candidate):
                result.add(candidate)
    return result