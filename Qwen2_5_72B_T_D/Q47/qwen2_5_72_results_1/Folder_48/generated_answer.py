def palindromes_of_specific_lengths(s):

    def is_palindrome(x):
        return x.lower() == x[::-1].lower()
    substring = s[155:284]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 104, i + 121):
            if j <= len(substring):
                candidate = substring[i:j]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate)
    return palindromes