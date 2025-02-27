def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    relevant_substring = s[65:100]
    palindromes = set()
    for length in range(26, 34):
        for start in range(len(relevant_substring) - length + 1):
            candidate = relevant_substring[start:start + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate.lower())
    return palindromes