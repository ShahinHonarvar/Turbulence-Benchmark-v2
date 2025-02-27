def palindromes_of_specific_lengths(s):

    def is_valid_palindrome(p):
        return p.isalpha() and p.lower() == p[::-1].lower()
    valid_palindromes = set()
    substring = s[10:101]
    for i in range(len(substring)):
        for j in range(i + 10, min(i + 51, len(substring) + 1)):
            candidate = substring[i:j]
            if is_valid_palindrome(candidate):
                valid_palindromes.add(candidate.lower())
    return valid_palindromes