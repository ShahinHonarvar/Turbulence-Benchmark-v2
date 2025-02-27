def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_palindromes = set()
    substring = s[17:73]
    for i in range(len(substring)):
        for j in range(i + 50, i + 52):
            if j <= len(substring):
                candidate = substring[i:j]
                if candidate.isalpha() and is_palindrome(candidate):
                    valid_palindromes.add(candidate)
    return valid_palindromes