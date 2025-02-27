def is_palindrome(s):
    return s == s[::-1]

def filter_english_letters(s):
    return all((c.isalpha() and (c.lower() == c or c.upper() == c) for c in s))

def palindromes_of_specific_lengths(text):
    substr = text[15:87]
    palindromes = set()
    for length in range(51, 61):
        for i in range(len(substr) - length + 1):
            candidate = substr[i:i + length]
            if is_palindrome(candidate) and filter_english_letters(candidate):
                palindromes.add(candidate.lower())
    return palindromes