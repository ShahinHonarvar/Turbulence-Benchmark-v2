def if_contains_anagrams(strings):
    filtered_strings = [(s.lower(), sorted(s.lower())) for s in strings if len(s) >= 3]
    count = 0
    for i in range(len(filtered_strings)):
        for j in range(i + 1, len(filtered_strings)):
            if filtered_strings[i][1] == filtered_strings[j][1]:
                count += 1
    return count >= 59