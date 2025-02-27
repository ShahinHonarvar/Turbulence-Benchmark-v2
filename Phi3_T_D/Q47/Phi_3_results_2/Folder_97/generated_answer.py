def palindromes_of_specific_lengths(s):
    s = s[28:95].lower()

    def is_english_palindrome(word):
        for char in word:
            if not 'a' <= char <= 'z':
                return False
        return word == word[::-1]
    palindromes = set()
    for i in range(len(s)):
        for j in range(i + 38, min(i + 50, len(s)) + 1):
            sub = s[i:j]
            if is_english_palindrome(sub):
                palindromes.add(sub)
    return palindromes