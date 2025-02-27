def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_palindromes = set()
    for length in range(26, 30):
        for start in range(max(13, 0), min(100 - length + 1, len(s) - length + 1)):
            sub = s[start:start + length]
            if sub.isalpha() and is_palindrome(sub):
                valid_palindromes.add(sub.lower())
    return valid_palindromes