def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[:6]
    palindromes = set()
    for length in range(3, 6):
        for start in range(0, 6 - length + 1):
            part = substring[start:start + length]
            if part.isalpha() and is_palindrome(part):
                palindromes.add(part.lower())
    return palindromes