def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t.lower() == t[::-1].lower()
    valid_palindromes = set()
    substring = s[:31]
    for i in range(len(substring)):
        for j in range(i + 20, min(i + 31, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and is_palindrome(candidate):
                valid_palindromes.add(candidate.lower())
    return valid_palindromes