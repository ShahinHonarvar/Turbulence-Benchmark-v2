def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub[::-1].lower()
    substring = s[18:66]
    palindromes = set()
    for start in range(len(substring)):
        for end in range(start + 22, start + 37):
            if end < len(substring):
                candidate = substring[start:end + 1]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate.lower())
    return palindromes