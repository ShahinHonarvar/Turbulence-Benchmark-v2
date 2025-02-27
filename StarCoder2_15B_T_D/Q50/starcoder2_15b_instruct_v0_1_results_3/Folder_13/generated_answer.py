def if_contains_anagrams(strings):
    if not isinstance(strings, list) or not all((isinstance(s, str) for s in strings)):
        return False
    pairs = []
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) >= 3 and len(strings[j]) >= 3 and (sorted(strings[i].lower()) == sorted(strings[j].lower())):
                pairs.append((strings[i], strings[j]))
    return len(pairs) >= 144