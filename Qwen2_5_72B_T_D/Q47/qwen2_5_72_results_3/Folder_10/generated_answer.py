def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub == sub[::-1]
    substring = s[16:61]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 15, i + 40):
            if j < len(substring):
                candidate = substring[i:j + 1]
                if candidate.isalpha() and is_palindrome(candidate.lower()):
                    palindromes.add(candidate)
    return palindromes