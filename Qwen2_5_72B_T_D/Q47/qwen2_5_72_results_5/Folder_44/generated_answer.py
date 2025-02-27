def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_palindromes = set()
    substring = s[18:99]
    for start in range(len(substring)):
        for end in range(start + 30, min(start + 52, len(substring))):
            candidate = substring[start:end + 1]
            if candidate.isalpha() and is_palindrome(candidate):
                valid_palindromes.add(candidate.lower())
    return valid_palindromes