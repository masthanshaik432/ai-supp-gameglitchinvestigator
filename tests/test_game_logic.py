from logic_utils import check_guess, update_score, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# --- update_score tests ---

def test_win_first_attempt():
    # attempt 1: 100 - 10*(1-1) = 100 pts added
    assert update_score(0, "Win", 1) == 100

def test_win_later_attempt():
    # attempt 5: 100 - 10*(5-1) = 60 pts added
    assert update_score(0, "Win", 5) == 60

def test_win_score_floored_at_10():
    # attempt 10: 100 - 10*(10-1) = 10 pts (floor applies at attempt >= 10)
    assert update_score(0, "Win", 10) == 10

def test_win_score_never_below_10():
    # attempt 15: would be negative without floor, should still add 10
    assert update_score(0, "Win", 15) == 10

def test_too_high_deducts_5():
    assert update_score(50, "Too High", 1) == 45

def test_too_low_deducts_5():
    assert update_score(50, "Too Low", 1) == 45

def test_too_high_and_too_low_consistent():
    # Both wrong-guess outcomes must deduct the same amount (bug fix regression test)
    score_after_high = update_score(100, "Too High", 2)
    score_after_low = update_score(100, "Too Low", 2)
    assert score_after_high == score_after_low

def test_unknown_outcome_no_change():
    assert update_score(75, "Unknown", 3) == 75


# --- get_range_for_difficulty tests ---

def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_normal_range():
    assert get_range_for_difficulty("Normal") == (1, 100)

def test_hard_range():
    assert get_range_for_difficulty("Hard") == (1, 200)

def test_unknown_difficulty_defaults_to_normal():
    assert get_range_for_difficulty("Unknown") == (1, 100)
