def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substring = s[45:99]
    palindromes = set()
    for length in range(40, 48):
        for start in range(len(substring) - length + 1):
            part = substring[start:start + length]
            if part.isalpha() and is_palindrome(part):
                palindromes.add(part)
    return palindromes