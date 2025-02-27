def palindromes_between_indices(s):
    indices = s[2:9].lower()
    unique_chars = set(indices)
    result = set()
    for i in range(len(indices)):
        for j in range(i, len(indices)):
            for k in range(i, len(indices)):
                for l in range(i, len(indices)):
                    for m in range(i, len(indices)):
                        for n in range(i, len(indices)):
                            for o in range(i, len(indices)):
                                chars = [indices[i], indices[j], indices[k], indices[l], indices[m], indices[n], indices[o]]
                                if len(set(chars)) == len(unique_chars) and chars == chars[::-1]:
                                    result.add(''.join(chars))
    return result