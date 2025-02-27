def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    if len(s) < 88:
        return set()
    substring = s[11:88]
    palindromes = set()
    for i in range(len(substring)):
        for length in range(4, 6):
            if i + length <= len(substring):
                sub = substring[i:i + length]
                if sub.isalpha() and is_palindrome(sub):
                    palindromes.add(sub.lower())
    return palindromes