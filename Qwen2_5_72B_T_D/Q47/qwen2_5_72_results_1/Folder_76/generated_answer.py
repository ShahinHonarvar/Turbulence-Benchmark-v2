def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substring = s[101:293]
    valid_palindromes = set()
    for start in range(len(substring)):
        for end in range(start + 154, min(start + 183, len(substring) + 1)):
            candidate = substring[start:end]
            if candidate.isalpha() and is_palindrome(candidate):
                valid_palindromes.add(candidate)
    return valid_palindromes