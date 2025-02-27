from itertools import permutations

def palindromes_between_indices(s):
    section = s[6:10].lower()
    letter_counts = {}
    for letter in section:
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    palindromes = set()

    def find_palindromes(current_string, counts):
        if len(current_string) >= 4 and current_string == current_string[::-1]:
            palindromes.add(current_string)
        for letter, count in counts.items():
            if count > 0:
                counts[letter] -= 1
                find_palindromes(current_string + letter, counts)
                counts[letter] += 1
    find_palindromes('', letter_counts)
    return palindromes