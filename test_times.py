import pytest
from times import compute_overlap_time, time_range

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected

def test_no_overlap1():
    range1 = [("2010-01-12 10:00:00", "2010-01-12 10:15:00")]
    range2 = [("2010-01-12 10:20:00", "2010-01-12 10:30:00")]
    expected = []
    assert compute_overlap_time(range1, range2) == expected

def test_no_overlap2():
    range1 = [("2010-01-12 10:00:00", "2010-01-12 10:15:00")]
    range2 = [("2010-01-12 12:00:00", "2010-01-13 12:15:00")]
    expected = []
    assert compute_overlap_time(range1, range2) == expected

def test_several_interval_ranges():
    range1 = time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 2)
    range2 = time_range("2010-01-12 10:30:00", "2010-01-12 11:30:00", 2)
    expected = [('2010-01-12 10:30:00', '2010-01-12 11:00:00')]
    assert compute_overlap_time(range1, range2) == expected

def end_when_start():
    range1 = [("2010-01-12 10:00:00", "2010-01-12 10:30:00")]
    range2 = [("2010-01-12 10:30:00", "2010-01-12 11:00:00")]
    expected = []
    assert compute_overlap_time(range1, range2) == expected

test_generic_case()

with pytest.raises(ValueError, match="No overlap between the two time ranges"):
    test_no_overlap1()
    test_no_overlap2()
    end_when_start()

test_several_interval_ranges()


