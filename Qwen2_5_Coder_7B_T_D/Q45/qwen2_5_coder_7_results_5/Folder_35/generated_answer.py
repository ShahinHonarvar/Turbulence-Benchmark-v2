def palindromes_between_indices(s):
    letters = s[2:5]
    unique_letters = set(letters.lower())
    palindromes = set()

    def is_palindrome(word):
        return word == word[::-1]
    for i in range(len(unique_letters)):
        for j in range(i, len(unique_letters)):
            for k in range(j, len(unique_letters)):
                for l in range(k, len(unique_letters)):
                    word = ''.join(sorted([list(unique_letters)[i], list(unique_letters)[j], list(unique_letters)[k], list(unique_letters)[l]]))
                    if len(word) >= 4 and is_palindrome(word):
                        palindromes.add(word)
    return palindromes