def palindromes_between_indices(string):
    sub_string = string[7:10].lower()
    english_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    permutations = set()
    for i in range(len(english_letters)):
        for j in range(i + 1, len(english_letters)):
            for k in range(j + 1, len(english_letters)):
                permutations.add(english_letters[i] + english_letters[j] + english_letters[k])
    palindromes = set()
    for permutation in permutations:
        if permutation in sub_string:
            palindromes.add(permutation + permutation[::-1])
    return palindromes