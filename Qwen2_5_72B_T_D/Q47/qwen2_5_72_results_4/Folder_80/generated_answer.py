def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    relevant_substring = text[35:89]
    palindromes = set()
    for start in range(len(relevant_substring)):
        for end in range(start + 24, start + 34):
            if end > len(relevant_substring):
                break
            candidate = relevant_substring[start:end]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                palindromes.add(candidate)
    return palindromes