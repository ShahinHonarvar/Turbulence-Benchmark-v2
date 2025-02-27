def is_palindrome_of_letters(s):
    return s == s[::-1] and all((c.isalpha() for c in s))

def find_palindromes_in_range(s, start, end):
    for i in range(start, end + 1):
        for j in range(end, start - 1, -1):
            substr = s[i:j + 1]
            if is_palindrome_of_letters(substr):
                yield substr
            if j < i + 2:
                break

def palindromes_of_specific_lengths(s):
    return {palindrome for length in range(13, 41) for palindrome in find_palindromes_in_range(s.lower(), 23, 77) if len(palindrome) == length}