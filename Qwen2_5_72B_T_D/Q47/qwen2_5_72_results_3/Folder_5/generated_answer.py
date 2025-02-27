def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substr = s[63:71]
    palindromes = set()
    for length in range(4, 6):
        for start in range(len(substr) - length + 1):
            part = substr[start:start + length]
            if part.isalpha() and is_palindrome(part):
                palindromes.add(part)
    return palindromes