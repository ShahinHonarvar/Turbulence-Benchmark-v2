import itertools

def palindromes_between_indices(string):
    text_specification = "<Write a function called 'palindromes_between_indices' that takes one argument, which is a string. The given string may consist of any character. The function should return the set of all palindromes of the length of at least 3 such that each palindrome is created from any possible arrangement of the English letters in the given string that occur between index 1 to index 6, both inclusive. If no such palindromes of the specified length can be created from the English letters of the given string that occur in the specified range, the function should return an empty set. The function should form each palindrome in a case-insensitive manner.>"
    english_letters = [letter for letter in string if letter.isalpha()]
    arrangements = itertools.permutations(english_letters[1:7], 6)
    palindromes = set()
    for arrangement in arrangements:
        if len(arrangement) >= 3 and arrangement == arrangement[::-1]:
            palindromes.add(''.join(arrangement))
    return palindromes