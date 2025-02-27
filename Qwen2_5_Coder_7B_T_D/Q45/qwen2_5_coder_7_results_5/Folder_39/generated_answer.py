def palindromes_between_indices(s):
    arr = s[2:6]
    arr = arr.lower()
    arr = [char for char in arr if char.isalpha()]
    unique_chars = set(arr)
    palindromes = set()
    for i in range(len(unique_chars)):
        for j in range(i, len(unique_chars)):
            for k in range(j, len(unique_chars)):
                for l in range(k, len(unique_chars)):
                    for m in range(l, len(unique_chars)):
                        word = unique_chars[i] + unique_chars[j] + unique_chars[k] + unique_chars[l] + unique_chars[m]
                        if word == word[::-1] and len(word) >= 3:
                            palindromes.add(word)
    return palindromes