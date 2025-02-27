def is_palindrome(s):
    return s == s[::-1]

def is_valid_letter(c):
    return 'a' <= c <= 'z'

def palindromes_of_specific_lengths(s):
    substring = s[26:91]
    result = set()
    length = len(substring)
    for index in range(length - 26):
        substr = substring[index:index + 27]
        if len(substr) > 58:
            break
        if is_palindrome(substr.lower()) and all((is_valid_letter(c) for c in substr)):
            result.add(substr.lower())
    return result