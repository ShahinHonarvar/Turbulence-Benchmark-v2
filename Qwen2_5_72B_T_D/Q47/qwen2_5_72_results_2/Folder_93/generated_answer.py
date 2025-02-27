def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    potential_palindromes = set()
    s = s[17:96]
    for i in range(len(s)):
        for j in range(i + 13, min(i + 50, len(s) + 1)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                potential_palindromes.add(substring)
    return potential_palindromes