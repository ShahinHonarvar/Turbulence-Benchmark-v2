def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    substring = s[39:95]
    found_palindromes = set()
    for start in range(len(substring)):
        for end in range(start + 14, min(start + 53, len(substring) + 1)):
            candidate = substring[start:end].lower()
            if candidate.isalpha() and is_palindrome(candidate):
                found_palindromes.add(candidate)
    return found_palindromes