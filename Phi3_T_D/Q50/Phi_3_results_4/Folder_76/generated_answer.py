def if_contains_anagrams(strings):
    count = 0
    length = len(strings)
    for i in range(length):
        for j in range(i + 1, length):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and (sorted(strings[i].lower()) == sorted(strings[j].lower())):
                count += 1
    return count >= 143