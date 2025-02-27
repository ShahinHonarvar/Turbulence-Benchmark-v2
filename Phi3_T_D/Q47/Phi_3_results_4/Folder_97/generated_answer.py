def is_palindrome(s):
    return s == s[::-1]

def create_all_substrings(s, min_length, max_length):
    substrings = set()
    for i in range(len(s) - max_length + 1):
        for length in range(min_length, max_length + 1):
            if i + length > len(s):
                break
            substring = s[i:i + length]
            if all((c.isalpha() for c in substring)):
                substrings.add(substring)
    return substrings

def palindromes_of_specific_lengths(s):
    if len(s) < 53:
        return set()
    substrings = create_all_substrings(s[28:95], 38, 49)
    return {sub for sub in substrings if is_palindrome(sub)}