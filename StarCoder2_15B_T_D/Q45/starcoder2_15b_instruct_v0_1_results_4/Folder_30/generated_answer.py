def palindromes_between_indices(string: str) -> set:
    letters = {letter for letter in string.lower() if letter.isalpha() and 0 <= string.index(letter) <= 4}
    palindromes = set()
    for length in range(4, len(letters) + 1):
        for i in range(len(letters) - length + 1):
            palindrome = ''.join(sorted(letters)[i:i + length])
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes