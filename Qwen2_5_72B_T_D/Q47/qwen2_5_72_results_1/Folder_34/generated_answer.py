def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[200:301]
    palindromes = set()
    for length in range(10, 51):
        for i in range(len(substring) - length + 1):
            potential_palindrome = substring[i:i + length]
            if potential_palindrome.isalpha() and is_palindrome(potential_palindrome):
                palindromes.add(potential_palindrome)
    return palindromes