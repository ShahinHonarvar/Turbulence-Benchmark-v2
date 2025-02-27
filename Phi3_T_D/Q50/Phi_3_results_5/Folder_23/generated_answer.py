def if_contains_anagrams(str_list):
    counts = {}
    for s in str_list:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in counts:
                counts[sorted_str] += 1
            else:
                counts[sorted_str] = 1
    return sum((v * (v - 1) // 2 for v in counts.values())) >= 67