def palindromes_of_specific_lengths(s):
    substring = s[23:95]
    english_letters = set('abcdefghijklmnopqrstuvwxyz')

    def is_palindrome(word):
        return word.lower() == word[::-1].lower()
    return {word[i:i + length] for length in range(17, 56) for i in range(len(substring) - length + 1) if set(word[i:i + length].lower()) <= english_letters and is_palindrome(word[i:i + length])}