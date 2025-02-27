def palindromes_between_indices(s):
    letters = s[3:10]
    letters = ''.join(filter(str.isalpha, letters)).lower()
    unique_letters = ''.join(sorted(set(letters)))
    result = set()
    for i in range(len(unique_letters)):
        for j in range(i, len(unique_letters)):
            for k in range(j, len(unique_letters)):
                for l in range(k, len(unique_letters)):
                    for m in range(l, len(unique_letters)):
                        for n in range(m, len(unique_letters)):
                            for o in range(n, len(unique_letters)):
                                candidate = unique_letters[i] + unique_letters[j] + unique_letters[k] + unique_letters[l] + unique_letters[m] + unique_letters[n] + unique_letters[o]
                                if candidate == candidate[::-1]:
                                    result.add(candidate)
    return result