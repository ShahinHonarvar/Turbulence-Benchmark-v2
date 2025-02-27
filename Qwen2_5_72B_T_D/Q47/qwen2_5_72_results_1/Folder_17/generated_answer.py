def palindromes_of_specific_lengths(s):

    def is_palindrome(t):
        return t == t[::-1]
    relevant_substring = s[22:96]
    found_palindromes = set()
    for length in range(52, 56):
        for start in range(len(relevant_substring) - length + 1):
            candidate = relevant_substring[start:start + length]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                found_palindromes.add(candidate)
    return found_palindromes