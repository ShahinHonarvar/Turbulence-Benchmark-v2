def is_palindrome(s):
    return s == s[::-1]

def char_is_letter(c):
    return 'a' <= c <= 'z' or 'A' <= c <= 'Z'

def palindromes_of_specific_lengths(s):
    substring = s[18:99]
    palindromes = set()
    length = len(substring)
    upper_limit = min(length, 51)
    lower_limit = max(31 - (51 - length), 1)
    for i in range(lower_limit, upper_limit + 1):
        for j in range(length - i + 1):
            candidate = substring[j:j + i]
            if all((char_is_letter(c) for c in candidate)) and is_palindrome(candidate.lower()):
                palindromes.add(candidate)
    return palindromes