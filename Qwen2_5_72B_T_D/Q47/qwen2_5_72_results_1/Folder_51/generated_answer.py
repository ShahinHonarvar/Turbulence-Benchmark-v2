def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    substring = s[2:9]
    palindromes = set()
    for i in range(len(substring)):
        for j in range(i + 3, i + 5):
            if j <= len(substring):
                candidate = substring[i:j]
                if candidate.isalpha() and is_palindrome(candidate):
                    palindromes.add(candidate.lower())
    return palindromes