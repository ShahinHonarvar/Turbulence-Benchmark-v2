def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    palindromes = set()
    substring = s[:10]
    for length in range(3, 6):
        for i in range(len(substring) - length + 1):
            candidate = substring[i:i + length]
            if candidate.isalpha() and is_palindrome(candidate):
                palindromes.add(candidate.lower())
    return palindromes