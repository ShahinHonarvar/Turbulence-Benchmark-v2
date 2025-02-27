def palindromes_of_specific_lengths(string):

    def is_palindrome(s):
        return s == s[::-1]
    palindromes = set()
    substring = string[32:80]
    for i in range(len(substring)):
        for j in range(i + 35, i + 42):
            if j <= len(substring):
                candidate = substring[i:j].lower()
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes