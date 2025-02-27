def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    s = s[:51]
    palindromes = set()
    for start in range(len(s)):
        for end in range(start + 50, min(start + 101, len(s) + 1)):
            candidate = s[start:end]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes