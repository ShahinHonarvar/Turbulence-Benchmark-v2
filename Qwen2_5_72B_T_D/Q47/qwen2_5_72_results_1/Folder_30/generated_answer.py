def palindromes_of_specific_lengths(s):

    def is_palindrome(string):
        return string.lower() == string.lower()[::-1]
    substring = s[14:91]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 55, i + 72):
            if j <= len(substring):
                candidate = substring[i:j]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes