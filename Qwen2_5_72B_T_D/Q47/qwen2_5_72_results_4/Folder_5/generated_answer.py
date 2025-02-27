def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substring = s[63:71]
    palindromes = set()
    for i in range(len(substring) - 3):
        for length in range(4, 6):
            if i + length <= len(substring):
                sub = substring[i:i + length]
                if sub.isalpha() and is_palindrome(sub):
                    palindromes.add(sub.lower())
    return palindromes