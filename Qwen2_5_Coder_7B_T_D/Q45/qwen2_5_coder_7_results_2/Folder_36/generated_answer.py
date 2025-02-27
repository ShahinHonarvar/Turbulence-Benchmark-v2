def palindromes_between_indices(s):
    letters = [char.lower() for char in s[5:9]]
    unique_letters = set(letters)
    palindromes = set()
    for i in range(len(unique_letters)):
        for j in range(i, len(unique_letters)):
            for k in range(j, len(unique_letters)):
                for l in range(k, len(unique_letters)):
                    for m in range(l, len(unique_letters)):
                        for n in range(m, len(unique_letters)):
                            candidate = ''.join(sorted([unique_letters[i], unique_letters[j], unique_letters[k], unique_letters[l], unique_letters[m], unique_letters[n]]))
                            if candidate == candidate[::-1] and len(candidate) >= 3:
                                palindromes.add(candidate)
    return palindromes