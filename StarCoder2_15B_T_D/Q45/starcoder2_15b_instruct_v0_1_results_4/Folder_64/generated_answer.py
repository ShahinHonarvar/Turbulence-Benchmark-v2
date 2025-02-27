import itertools

def palindromes_between_indices(string):
    letters = [c for c in string.lower() if c.isalpha() and 4 <= string.index(c) <= 9]
    arrangements = itertools.permutations(letters)
    palindromes = set()
    for arrangement in arrangements:
        word = ''.join(arrangement)
        if len(word) >= 5 and word == word[::-1]:
            palindromes.add(word)
    return palindromes