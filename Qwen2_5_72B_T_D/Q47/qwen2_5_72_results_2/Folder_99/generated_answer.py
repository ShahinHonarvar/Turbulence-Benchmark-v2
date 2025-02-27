def palindromes_of_specific_lengths(s):

    def is_palindrome(p):
        return p.lower() == p[::-1].lower()
    substring = s[127:289]
    palindromes_set = set()
    for length in range(119, 142):
        for i in range(len(substring) - length + 1):
            part = substring[i:i + length]
            if part.isalpha() and is_palindrome(part):
                palindromes_set.add(part)
    return palindromes_set