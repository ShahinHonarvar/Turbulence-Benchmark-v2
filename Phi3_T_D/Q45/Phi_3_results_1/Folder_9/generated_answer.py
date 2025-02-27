def generate_substrings(s, min_length):
    if not s or len(s) < min_length:
        return []
    substrings = set()
    for i in range(len(s) - min_length + 1):
        substrings.add(s[i:i + min_length])
    return substrings

def is_palindrome(s):
    return s.lower() == s[::-1].lower()

def palindromes_between_indices(s):
    palindromes = set()
    index_range = s[:7]
    substrings = generate_substrings(index_range, 7)
    for substr in substrings:
        if is_palindrome(substr):
            palindromes.add(substr)
    return palindromes