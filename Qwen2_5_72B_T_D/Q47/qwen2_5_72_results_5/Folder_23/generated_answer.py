def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    specified_substring = s[23:95]
    palindromes = set()
    for start in range(len(specified_substring)):
        for end in range(start + 17, min(start + 56, len(specified_substring) + 1)):
            candidate = specified_substring[start:end]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes