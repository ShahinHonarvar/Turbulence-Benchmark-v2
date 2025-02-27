def palindromes_of_specific_lengths(s):

    def is_palindrome(seq):
        return seq == seq[::-1]
    substring = s[62:89].lower()
    palindromes = set()
    for length in range(18, 22):
        for i in range(len(substring) - length + 1):
            part = substring[i:i + length]
            if part.isalpha() and is_palindrome(part):
                palindromes.add(part)
    return palindromes