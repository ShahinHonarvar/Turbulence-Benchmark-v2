def is_palindrome(s):
    """Check if the string s is a palindrome."""
    return s == s[::-1]

def generate_substrings(s):
    """Generate all substrings of s."""
    length = len(s)
    return [s[i:j] for i in range(length) for j in range(i + 1, length + 1)]

def palindrome_of_length_at_least_n(s):
    result = set()
    s = s.lower()
    substrings = generate_substrings(s)
    for sub in substrings:
        if len(sub) >= 92 and is_palindrome(sub):
            result.add(sub)
    return result