def palindromes_between_indices(string):
    letters = sorted(set(string[4:10].lower()))
    palindromes = set()
    for length in range(7, len(letters) + 1):
        generate_palindromes(letters, length, [], palindromes)
    return palindromes

def generate_palindromes(letters, length, current, palindromes):
    if len(current) == length:
        palindrome = ''.join(current)
        if palindrome == palindrome[::-1]:
            palindromes.add(palindrome)
    else:
        for i, letter in enumerate(letters):
            current.append(letter)
            generate_palindromes(letters[i + 1:], length, current, palindromes)
            current.pop()