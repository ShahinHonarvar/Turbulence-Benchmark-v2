def generate_palindrome_candidates(s):
    candidates = set()
    for i in range(len(s)):
        for j in range(i + 49, min(i + 52, len(s) + 1)):
            if s[i:j].isalpha() and 'a' <= s[i].lower() <= 'z' and ('a' <= s[j - 1].lower() <= 'z'):
                candidates.add(s[i:j].lower())
    return candidates

def palindromes_of_specific_lengths(s):
    start_idx, end_idx = (17, 72)
    substr = s[start_idx:end_idx + 1]
    candidates = generate_palindrome_candidates(substr)
    return {candidate for candidate in candidates if candidate == candidate[::-1]}