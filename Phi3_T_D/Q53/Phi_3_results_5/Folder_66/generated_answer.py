def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(text):
    text = text.lower()
    palindromes = set()
    for start in range(len(text)):
        for length in range(76, len(text) - start + 1):
            candidate = text[start:start + length]
            if is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes