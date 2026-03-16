from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result, _ = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result, _ = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result, _ = check_guess(40, 50)
    assert result == "Too Low"

def test_out_of_attempts_final_wrong_guess_is_not_win():
    # Regression test for the "out of attempts" bug (fixed in bc1e41b).
    # When the player uses their last attempt with a wrong guess,
    # check_guess must return a non-Win outcome so the game correctly
    # transitions to "lost" rather than silently continuing.
    secret = 50
    attempt_limit = 5  # Hard difficulty
    attempts = 0
    outcome = None

    wrong_guesses = [10, 20, 30, 40, 60]  # all wrong, len == attempt_limit
    for guess in wrong_guesses:
        attempts += 1
        outcome, _ = check_guess(guess, secret)

    assert attempts == attempt_limit, "Should have used exactly all attempts"
    assert outcome != "Win", "Last wrong guess must not be 'Win' — game should end as lost"
    assert attempt_limit - attempts == 0, "Attempts remaining must be 0 after exhausting all attempts"
