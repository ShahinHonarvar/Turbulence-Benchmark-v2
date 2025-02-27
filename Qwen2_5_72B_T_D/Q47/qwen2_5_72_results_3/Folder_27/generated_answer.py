def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    valid_palindromes = set()
    substring = s[13:100]
    for i in range(len(substring)):
        for j in range(26, 30):
            if i + j <= len(substring):
                candidate = substring[i:i + j]
                if candidate.isalpha() and is_palindrome(candidate):
                    valid_palindromes.add(candidate.lower())
    return valid_palindromes