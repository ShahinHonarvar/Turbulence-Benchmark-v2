def palindrome_of_length_at_least_n(s):
    candidates = {s[i:i + j] for i in range(len(s)) for j in range(26, len(s) - i + 1)}
    palindromes = {candidate for candidate in candidates if candidate.lower() == candidate.lower()[::-1] and candidate.isalpha()}
    return set(filter(lambda x: len(x) >= 26, palindromes))