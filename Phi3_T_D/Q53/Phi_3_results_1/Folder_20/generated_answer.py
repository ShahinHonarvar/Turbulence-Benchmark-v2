def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def get_palindromes(s, length):
    n = len(s)
    result = set()
    for i in range(n):
        for j in range(i + length, n + 1):
            if is_palindrome(s[i:j]):
                result.add(s[i:j])
    return result

def palindrome_of_length_at_least_n(s):
    length = 66
    return get_palindromes(s, length)