def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    specified_substring = s[15:73]
    found_palindromes = set()
    for start in range(len(specified_substring)):
        for end in range(start + 19, min(start + 56, len(specified_substring) + 1)):
            candidate = specified_substring[start:end]
            if candidate.isalpha() and is_palindrome(candidate):
                found_palindromes.add(candidate.lower())
    return found_palindromes