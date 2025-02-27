from itertools import permutations
import string

def is_palindrome(word):
    return word == word[::-1]

def palindromes_between_indices(s):
    substring = s[6:9]
    letter_counts = {letter: substring.lower().count(letter) for letter in string.ascii_lowercase}
    possible_palindromes = set()
    for center in letter_counts:
        while letter_counts[center] > 0:
            for other_center in letter_counts:
                if center != other_center:
                    for times in range(letter_counts[other_center]):
                        possible_palindromes.add(center.upper() + ''.join(['{}{}'.format(letter, letter) for letter in letter_counts if letter != center and letter != other_center]) + other_center.upper())
            letter_counts[center] -= 1
    return {palindrome for palindrome in possible_palindromes if is_palindrome(palindrome)}