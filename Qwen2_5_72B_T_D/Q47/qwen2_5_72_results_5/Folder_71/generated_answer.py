def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    specified_substring = s[18:66]
    palindromes_set = set()
    for start in range(len(specified_substring)):
        for end in range(start + 23, min(start + 37, len(specified_substring) + 1)):
            candidate = specified_substring[start:end]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes_set.add(candidate.lower())
    return palindromes_set