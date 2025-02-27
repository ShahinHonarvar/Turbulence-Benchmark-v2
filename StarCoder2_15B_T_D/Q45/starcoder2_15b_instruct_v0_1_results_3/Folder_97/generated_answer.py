def palindromes_between_indices(string):
    count_letters = {}
    for i in range(0, 5):
        letter = string[i].lower()
        if letter.isalpha():
            count_letters[letter] = count_letters.get(letter, 0) + 1
    palindromes = set()
    for letter in count_letters:
        if count_letters[letter] >= 2:
            palindromes.add(letter * 2)
    return palindromes