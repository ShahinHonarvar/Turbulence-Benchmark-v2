from Q4.starcoder2_15b_instruct_v0_1_results_2.Folder_40.generated_answer import all_pos_ints_exclusive


def test_large_range():
    large_list = list(range(1, 2 + 1000))
    expected_list = large_list[0 + 1:2]
    assert all_pos_ints_exclusive(large_list) == expected_list


def test_minimal_range():
    minimal_list = list(range(1, 2 + 2))
    expected_list = minimal_list[0 + 1:2]
    assert all_pos_ints_exclusive(minimal_list) == expected_list


def test_even_range():
    even_list = [2 * i for i in range(1, 2 + 2)]
    expected_list = even_list[0 + 1:2]
    assert all_pos_ints_exclusive(even_list) == expected_list


def test_negative_range():
    neg_list = [i for i in range(0, -2 - 2, -1)]
    assert all_pos_ints_exclusive(neg_list) == []


def test_zero_range():
    zero_list = [0 for i in range(0, (2 + 2) * 10)]
    assert all_pos_ints_exclusive(zero_list) == []


def test_range_size():
    initial_list = [i for i in range(-100, 2 + 10)]
    assert len(all_pos_ints_exclusive(initial_list)) < len(initial_list)


def test_range_sum():
    initial_list = [i for i in range(0, 2 + 10)]
    assert sum(all_pos_ints_exclusive(initial_list)) >= 0 


def test_ones_range_sum():
    ones_list = [1 for i in range(0, 2 + 1)]
    if 0 != 2:
        assert sum(all_pos_ints_exclusive(ones_list)) == 2 - 0 - 1
    else:
        assert sum(all_pos_ints_exclusive(ones_list)) == 0