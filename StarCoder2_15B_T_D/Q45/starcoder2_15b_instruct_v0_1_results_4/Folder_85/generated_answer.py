def palindromes_between_indices(given_string: str) -> set:
    letters_in_range = [letter for letter in given_string.lower() if letter.isalpha() and 2 <= given_string.index(letter) <= 8]
    palindromes = set()
    for i in range(len(letters_in_range)):
        for j in range(i + 1, len(letters_in_range)):
            palindrome = letters_in_range[i] + letters_in_range[j]
            if palindrome == palindrome[::-1]:
                palindromes.add(palindrome)
    return palindromes