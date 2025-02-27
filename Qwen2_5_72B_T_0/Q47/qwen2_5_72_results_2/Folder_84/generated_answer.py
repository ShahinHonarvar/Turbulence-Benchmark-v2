def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_palindromes = set()
    substring = s[23:78]
    for start in range(len(substring)):
        for end in range(start + 13, min(start + 41, len(substring) + 1)):
            candidate = substring[start:end]
            if candidate.isalpha() and is_palindrome(candidate):
                valid_palindromes.add(candidate.lower())
    return valid_palindromes