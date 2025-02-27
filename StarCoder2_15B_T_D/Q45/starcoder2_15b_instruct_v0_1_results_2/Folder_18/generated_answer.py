import itertools

def palindromes_between_indices(string):
    string = string.lower()
    characters = [char for i, char in enumerate(string) if 1 <= i <= 6]
    arrangements = itertools.permutations(characters)
    palindromes = set()
    for arrangement in arrangements:
        palindrome = ''.join(arrangement) + ''.join(arrangement[::-1])
        if len(palindrome) >= 3:
            palindromes.add(palindrome)
    return palindromes