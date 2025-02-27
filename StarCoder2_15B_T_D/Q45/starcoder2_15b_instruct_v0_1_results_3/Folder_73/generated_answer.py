import itertools

def palindromes_between_indices(s):
    letter_count = {}
    for letter in s:
        if letter.isalpha():
            letter_count[letter.lower()] = letter_count.get(letter.lower(), 0) + 1
    palindromes = set()
    for permutation in itertools.permutations(letter_count.keys(), 3):
        palindrome = ''.join(permutation)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    return palindromes