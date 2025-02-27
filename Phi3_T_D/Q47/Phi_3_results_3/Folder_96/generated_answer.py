def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(input_str):
    palindromes = set()
    for length in range(50, 101):
        for i in range(100, 301 - length + 1):
            candidate = input_str[i:i + length]
            if all((c.isalpha() for c in candidate)) and is_palindrome(candidate.lower()):
                palindromes.add(candidate.lower())
    return palindromes