def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_palindromes = set()
    substring = s[15:90]
    for i in range(len(substring)):
        for j in range(i + 40, i + 73):
            if j <= len(substring):
                candidate = substring[i:j]
                if candidate.isalpha() and is_palindrome(candidate):
                    valid_palindromes.add(candidate)
    return valid_palindromes