def palindromes_between_indices(s):
    filtered_chars = [char.lower() for char in s[:6] if char.isalpha()]
    unique_chars = set(filtered_chars)
    palindromes = set()
    for i in range(len(unique_chars)):
        for j in range(i, len(unique_chars)):
            for k in range(j, len(unique_chars)):
                for l in range(k, len(unique_chars)):
                    for m in range(l, len(unique_chars)):
                        candidate = unique_chars[i] + unique_chars[j] + unique_chars[k] + unique_chars[l] + unique_chars[m] + unique_chars[i]
                        if candidate == candidate[::-1] and len(candidate) >= 3:
                            palindromes.add(candidate)
    return palindromes