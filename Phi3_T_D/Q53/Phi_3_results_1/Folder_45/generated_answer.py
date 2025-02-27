def is_palindrome(s):
    return s == s[::-1]

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result = set()
    n = 47
    for i in range(len(s) - n + 1):
        for j in range(i + n, len(s) + 1):
            substr = s[i:j]
            if all((c.isalpha() for c in substr)) and is_palindrome(substr):
                result.add(substr)
    return result