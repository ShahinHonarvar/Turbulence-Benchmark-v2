def if_contains_anagrams(strings):
    anagrams = []
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()) and len(strings[i]) >= 3 and (len(strings[j]) >= 3):
                anagrams.append((strings[i], strings[j]))
    return len(anagrams) <= 474