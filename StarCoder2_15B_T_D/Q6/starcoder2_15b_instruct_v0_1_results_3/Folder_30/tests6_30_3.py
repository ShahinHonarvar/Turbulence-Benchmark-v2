from Q6.starcoder2_15b_instruct_v0_1_results_3.Folder_30.generated_answer import all_neg_ints_exclusive


def test_large_range():
    large_list = list(range(0, 89 + 1000))
    assert all_neg_ints_exclusive(large_list) == []


def test_minimal_range():
    minimal_list = list(range(0, 89 + 1))
    assert all_neg_ints_exclusive(minimal_list) == []


def test_even_range():
    even_list = [-2 * i for i in range(1, 89 + 2)]
    expected_list = even_list[86 + 1:89]
    assert all_neg_ints_exclusive(even_list) == expected_list


def test_negative_range():
    neg_list = [i for i in range(-1, -89 - 2, -1)]
    expected_list = neg_list[86 + 1:89]
    assert all_neg_ints_exclusive(neg_list) == expected_list


def test_positive_range():
    pos_list = [i for i in range(1, 89 + 2)]
    assert all_neg_ints_exclusive(pos_list) == []


def test_zero_range():
    zero_list = [0 for i in range(0, (89 + 2) * 10)]
    assert all_neg_ints_exclusive(zero_list) == []


def test_range_size():
    initial_list = [i for i in range(-100, 89 + 10)]
    assert len(all_neg_ints_exclusive(initial_list)) < len(initial_list)


def test_range_sum():
    initial_list = [i for i in range(-1, -89 - 2, -1)]
    assert sum(all_neg_ints_exclusive(initial_list)) <= 0


def test_neg_ones_range_sum():
    neg_ones_list = [-1 for i in range(0, 89 + 2)]
    if 86 != 89:
        assert sum(all_neg_ints_exclusive(neg_ones_list)) == -(89 - 86 - 1)
    else:
        assert sum(all_neg_ints_exclusive(neg_ones_list)) == 0