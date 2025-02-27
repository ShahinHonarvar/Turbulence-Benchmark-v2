def if_contains_anagrams(strings):
    pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if sorted(strings[i].lower()) == sorted(strings[j].lower()) and len(strings[i]) >= 3 and (len(strings[j]) >= 3):
                pairs += 1
    return pairs >= 25