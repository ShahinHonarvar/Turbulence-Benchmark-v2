def is_palindrome(s):
    return s == s[::-1]

def palindromes_of_specific_lengths(input_string):
    result = set()
    for length in range(104, 121):
        for i in range(155, 284 - length + 1):
            substring = input_string[i:i + length]
            if all((c.isalpha() for c in substring)):
                trimmed_substring = substring.lower()
                if is_palindrome(trimmed_substring):
                    result.add(trimmed_substring)
    return result