def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    s = s[26:91]
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            candidate = s[start:end]
            if 27 <= len(candidate) <= 58 and candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes