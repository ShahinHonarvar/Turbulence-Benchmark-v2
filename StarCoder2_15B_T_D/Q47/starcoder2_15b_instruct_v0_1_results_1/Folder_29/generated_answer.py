def palindromes_of_specific_lengths(string):
    substring = string[15:95]

    def is_palindrome(substring):
        return substring.lower() == substring.lower()[::-1]
    palindromes = set()
    for length in range(18, 74):
        for i in range(len(substring) - length + 1):
            substring = substring[i:i + length]
            if is_palindrome(substring):
                palindromes.add(substring)
    return palindromes