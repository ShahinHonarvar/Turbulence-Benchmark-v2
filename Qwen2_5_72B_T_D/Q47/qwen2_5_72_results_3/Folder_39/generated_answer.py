def palindromes_of_specific_lengths(s):

    def is_palindrome(sub):
        return sub.lower() == sub.lower()[::-1]
    substring = s[31:92]
    palindromes = set()
    for start in range(len(substring)):
        for end in range(start + 50, start + 54):
            if end <= len(substring):
                candidate = substring[start:end]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes