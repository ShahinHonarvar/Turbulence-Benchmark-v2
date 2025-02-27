def palindromes_between_indices(text):
    letters = [letter for letter in text if letter.isalpha()]
    sub_letters = letters[7:9]
    palindromes = set()
    for i in range(len(sub_letters)):
        for j in range(i + 1, len(sub_letters)):
            palindrome = sub_letters[i] + sub_letters[j]
            if len(palindrome) >= 3:
                palindromes.add(palindrome)
    return palindromes