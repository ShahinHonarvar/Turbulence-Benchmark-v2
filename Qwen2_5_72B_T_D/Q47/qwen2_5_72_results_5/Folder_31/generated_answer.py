def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substring = s[11:84]
    palindromes = set()
    for start in range(len(substring)):
        for end in range(start + 36, start + 61):
            if end < len(substring):
                candidate = substring[start:end + 1]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes