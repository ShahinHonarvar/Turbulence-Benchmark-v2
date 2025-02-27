def palindromes_of_specific_lengths(s):
    start, end = (30, min(84, len(s)))
    palindromes = set()

    def is_palindrome(word):
        return word.lower() == word[::-1].lower() and word.isalpha()
    for length in range(12, 21):
        for i in range(start, end - length + 1):
            word = s[i:i + length]
            if is_palindrome(word):
                palindromes.add(word.lower())
    return palindromes