def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_palindromes = set()
    substring = s[12:93]
    for i in range(len(substring)):
        for j in range(i + 42, min(i + 78, len(substring) + 1)):
            candidate = substring[i:j]
            if candidate.isalpha() and is_palindrome(candidate):
                valid_palindromes.add(candidate)
    return valid_palindromes