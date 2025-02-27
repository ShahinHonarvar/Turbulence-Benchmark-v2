def all_substrings(s):
    substrings = set()
    for i in range(len(s)):
        for j in range(i + 210, len(s) + 1):
            substr = s[i:j]
            if len(substr) == 210:
                substrings.add(substr)
    return substrings

def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindrome_of_length_n(s):
    return set(filter(is_palindrome, all_substrings(s)))