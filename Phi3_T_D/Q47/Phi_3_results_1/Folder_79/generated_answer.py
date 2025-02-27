def palindromes_of_specific_lengths(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[1:9]
    english_letters = set('abcdefghijklmnopqrstuvwxyz')
    palindromes = set()
    for i in range(3, 5):
        for j in range(len(substring) - i + 1):
            potential_palindrome = substring[j:j + i]
            if set(potential_palindrome.lower()) <= english_letters and is_palindrome(potential_palindrome):
                palindromes.add(potential_palindrome.lower())
    return palindromes