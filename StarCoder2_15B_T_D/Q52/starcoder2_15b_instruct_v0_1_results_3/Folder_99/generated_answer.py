def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_n(s):
    result = set()
    for i in range(len(s) - 420 + 1):
        substring = s[i:i + 420]
        if is_palindrome(substring) and substring.isalpha():
            result.add(substring)
    return result