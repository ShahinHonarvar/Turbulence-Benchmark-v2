def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[29:97]
    valid_palindromes = set()
    for length in range(12, 19):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha() and is_palindrome(candidate):
                valid_palindromes.add(candidate)
    return valid_palindromes