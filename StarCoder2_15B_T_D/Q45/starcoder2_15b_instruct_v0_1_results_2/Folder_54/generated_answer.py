import string

def palindromes_between_indices(s):
    palindromes = set()
    for combination in string.ascii_letters:
        if combination[::-1].lower() == combination.lower() and len(combination) >= 4:
            palindromes.add(combination)
    return palindromes