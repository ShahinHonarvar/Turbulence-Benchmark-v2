from itertools import permutations

def palindromes_between_indices(s):

    def is_palindrome(word):
        return word == word[::-1]
    substring = s[:7].lower()
    letters = ''.join(filter(str.isalpha, substring))
    letter_count = {}
    for letter in letters:
        letter_count[letter] = letter_count.get(letter, 0) + 1
    if sum((v % 2 for v in letter_count.values())) <= 1:
        options = []
        for letter, count in letter_count.items():
            if count >= 2:
                options.extend([letter] * (count // 2))
            if count % 2 == 1:
                options.append(letter)
        palindromes = set((''.join(x) + ''.join(reversed(x)) for x in set(permutations(options))))
        palindromes = {s for s in palindromes if len(s) >= 6}
        return palindromes
    return set()