def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substring = s[28:95]
    palindromes = set()
    for length in range(38, 50):
        for i in range(len(substring) - length + 1):
            part = substring[i:i + length]
            if part.isalpha() and is_palindrome(part):
                palindromes.add(part)
    return palindromes