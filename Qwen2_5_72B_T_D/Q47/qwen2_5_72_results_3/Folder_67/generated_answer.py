def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substring = s[65:100]
    palindromes = set()
    for length in range(26, 34):
        for start in range(len(substring) - length + 1):
            candidate = substring[start:start + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes