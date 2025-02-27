import itertools

def valid_palindrome(s):
    s = s.lower()
    return s == s[::-1]

def palindromes_between_indices(text):
    start, end = (6, 10)
    subsequence = [c for c in text[start:end] if c.isalpha()]
    unique_subsequences = set(subsequence)
    palindromes = set()
    for length in range(5, len(unique_subsequences) + 1):
        for seq in itertools.permutations(unique_subsequences, length):
            candidate = ''.join(seq)
            if valid_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes