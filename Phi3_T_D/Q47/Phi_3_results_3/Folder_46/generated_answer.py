def is_palindrome(s):
    return s == s[::-1]

def filter_palindromes(s):
    palindromes = set()
    for i in range(11, 98):
        for length in range(29, 63):
            substr = s[i:i + length]
            if substr.isalpha() and len(substr) == length and is_palindrome(substr):
                palindromes.add(substr.lower())
    return palindromes

def palindromes_of_specific_lengths(s):
    return filter_palindromes(s)