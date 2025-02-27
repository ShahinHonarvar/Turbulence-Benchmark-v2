def is_palindrome(s):
    return s.lower() == s[::-1].lower() and all((c.isalpha() for c in s))

def find_palindromes(s, length, start=0):
    result = set()
    for i in range(start, len(s) - length + 1):
        fragment = s[i:i + length]
        if is_palindrome(fragment):
            result.add(fragment)
    return result

def palindrome_of_length_at_least_n(s):
    s = s.lower()
    result_set = set()
    n = 41
    while n <= len(s):
        result_set.update(find_palindromes(s, n))
        n += 2
    return result_set