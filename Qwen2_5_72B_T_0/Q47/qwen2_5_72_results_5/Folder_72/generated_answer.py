def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_palindromes = set()
    substring = s[26:91]
    for start in range(len(substring)):
        for end in range(start + 1, len(substring) + 1):
            candidate = substring[start:end]
            if 27 <= len(candidate) <= 58 and candidate.isalpha() and is_palindrome(candidate):
                valid_palindromes.add(candidate.lower())
    return valid_palindromes