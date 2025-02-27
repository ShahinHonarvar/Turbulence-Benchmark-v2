def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    valid_range = s[103:277]
    palindromes = set()
    for start in range(len(valid_range)):
        for end in range(start + 100, min(start + 170, len(valid_range) + 1)):
            candidate = valid_range[start:end]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate)
    return palindromes