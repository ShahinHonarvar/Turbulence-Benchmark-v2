def if_contains_anagrams(strings):
    filtered_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    n = len(filtered_strings)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if filtered_strings[i] == filtered_strings[j]:
                count += 1
                if count >= 89:
                    return True
    return False