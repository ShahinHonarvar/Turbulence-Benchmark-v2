def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    if len(s) < 91:
        return set()
    substring = s[14:91]
    palindromes = set()
    for start in range(len(substring)):
        for end in range(start + 55, start + 72):
            if end > len(substring):
                break
            candidate = substring[start:end]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate.lower())
    return palindromes