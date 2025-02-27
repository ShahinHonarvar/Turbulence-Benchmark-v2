def palindromes_of_specific_lengths(text):

    def is_palindrome(s):
        return s == s[::-1]
    substring = text[23:95].lower()
    valid_palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 17, min(i + 56, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and is_palindrome(candidate):
                valid_palindromes.add(candidate)
    return valid_palindromes