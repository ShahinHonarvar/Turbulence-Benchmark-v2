def palindromes_between_indices(string):
    valid_letters = [letter for letter in string.lower() if letter.isalpha() and 2 <= string.index(letter) <= 9]
    palindromes = set()
    for length in range(4, len(valid_letters) + 1):
        for i in range(len(valid_letters) - length + 1):
            palindrome = valid_letters[i:i + length]
            if palindrome == palindrome[::-1]:
                palindromes.add(''.join(palindrome))
    return palindromes