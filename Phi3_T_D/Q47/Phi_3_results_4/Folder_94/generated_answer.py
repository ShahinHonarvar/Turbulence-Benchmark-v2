def palindromes_of_specific_lengths(s):
    s = s[40:95]

    def is_palindrome(word):
        return word.lower() == word[::-1].lower() and word.isalpha()
    return set((word for word in map(s[i:j], range(45, 52), (i for i in range(len(s) - 44, len(s) - 40))) if is_palindrome(word)))