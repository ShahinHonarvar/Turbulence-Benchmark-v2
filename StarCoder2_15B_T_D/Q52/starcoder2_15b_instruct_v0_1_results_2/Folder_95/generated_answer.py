def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_n(s):
    n = 87
    result = set()
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if is_palindrome(substring) and substring.isalpha():
            result.add(substring)
    return result