def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word.lower() == word.lower()[::-1]
    valid_palindromes = set()
    substring = s[1:10]
    for i in range(1, 8):
        for j in range(i + 2, 8):
            candidate = substring[i:j + 1]
            if candidate.isalpha() and 3 <= len(candidate) <= 7 and is_palindrome(candidate):
                valid_palindromes.add(candidate.lower())
    return valid_palindromes