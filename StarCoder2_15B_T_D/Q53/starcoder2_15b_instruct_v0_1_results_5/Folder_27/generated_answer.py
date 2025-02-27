def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    for i in range(len(s) - 99):
        for j in range(i + 100, len(s) + 1):
            substring = s[i:j]
            if is_palindrome(substring) and substring.isalpha():
                result.add(substring)
    return result