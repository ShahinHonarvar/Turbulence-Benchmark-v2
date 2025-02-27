def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[63:71]
    palindromes = set()
    for length in [4, 5]:
        for i in range(len(substring) - length + 1):
            part = substring[i:i + length]
            if is_palindrome(part) and part.isalpha():
                palindromes.add(part)
    return palindromes