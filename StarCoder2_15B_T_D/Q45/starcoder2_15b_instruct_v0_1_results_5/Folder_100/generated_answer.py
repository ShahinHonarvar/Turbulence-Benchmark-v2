def palindromes_between_indices(s):
    letters = sorted(set(s[0:6].lower()))
    n = len(letters)
    palindromes = set()

    def generate_palindromes(letters, current, n):
        if len(current) == n:
            palindromes.add(''.join(current))
        else:
            for i in range(n):
                if letters[i] not in current:
                    current.append(letters[i])
                    generate_palindromes(letters, current, n)
                    current.pop()
    generate_palindromes(letters, [], n)
    return palindromes