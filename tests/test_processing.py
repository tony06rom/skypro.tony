from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(fix_origin_data, fix_sorted_executed, fix_sorted_canceled):
    assert filter_by_state(fix_origin_data, "EXECUTED") == fix_sorted_executed
    assert filter_by_state(fix_origin_data, "CANCELED") == fix_sorted_canceled
    assert filter_by_state(fix_origin_data) == fix_sorted_executed
    assert filter_by_state(fix_origin_data, "QWERTY") == []
    assert filter_by_state(fix_origin_data, "") == []


def test_sort_by_date(fix_origin_data, fix_sorted_true, fix_sorted_false):
    assert sort_by_date(fix_origin_data, True) == fix_sorted_true
    assert sort_by_date(fix_origin_data, False) == fix_sorted_false
    assert sort_by_date(fix_origin_data) == fix_sorted_true
