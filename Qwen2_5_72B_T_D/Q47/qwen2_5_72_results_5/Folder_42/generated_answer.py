def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_range = s[43:96]
    palindromes = set()
    for i in range(len(valid_range)):
        for j in range(i + 18, min(len(valid_range) + 1, i + 48)):
            candidate = valid_range[i:j]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes