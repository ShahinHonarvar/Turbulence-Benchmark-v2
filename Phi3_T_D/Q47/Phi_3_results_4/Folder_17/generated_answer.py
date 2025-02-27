def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(s):
    result = set()
    for i in range(22, 96):
        for length in range(52, 56):
            if i + length > len(s):
                break
            substring = s[i:i + length]
            if substring.isalpha() and is_palindrome(substring.lower()):
                result.add(substring)
    return result