def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    palindromes = set()
    for i in range(100, 201):
        for j in range(i + 5, min(i + 11, 202)):
            substring = s[i:j]
            if substring.isalpha() and is_palindrome(substring):
                palindromes.add(substring.lower())
    return palindromes