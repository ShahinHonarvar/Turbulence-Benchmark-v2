def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[101:293]
    palindromes = set()
    for start in range(len(substring)):
        for end in range(start + 154, min(start + 183, len(substring) + 1)):
            candidate = substring[start:end]
            if candidate.isalpha() and is_palindrome(candidate.lower()):
                palindromes.add(candidate)
    return palindromes