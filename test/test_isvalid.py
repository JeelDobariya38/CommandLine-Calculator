from App.app import is_valid

def test_valid_input():
    assert is_valid("3 + 5") == True
    assert is_valid("7 % 3 = 1") == True
    assert is_valid("x > 5") == False

def test_invalid_input():
    assert is_valid("2a + b") == False
    assert is_valid("3 & 4") == False
    assert is_valid("= 7") == False

def test_empty_input():
    assert is_valid("") == True

def test_whitespace_input():
    assert is_valid("   ") == True

def test_complex_valid_input():
    assert is_valid("((1 + 2) * 3) / 4 = 1.5") == True

def test_complex_invalid_input():
    assert is_valid("(3 + 4) * 2 =") == False

def test_edge_operators():
    assert is_valid("5 + 2 - 3 * 4 / 2 = 5") == True

def test_edge_numbers():
    assert is_valid("1234567890") == True

def test_mixed_operators():
    assert is_valid("1 + 2 * 3 - 4 / 2 = 5") == True

def test_special_characters():
    assert is_valid("@ $ #") == False

def test_starting_with_operator():
    assert is_valid("+ 3 * 5 = 15") == False

def test_valid_input_with_eval():
    assert is_valid("3 + 5") == True
    assert is_valid("7 % 3 = 1") == True
    assert is_valid("x > 5") == False

def test_invalid_input_with_eval():
    assert is_valid("2a + b") == False
    assert is_valid("3 & 4") == False
    assert is_valid("= 7") == False

def test_valid_input_with_eval_complex():
    assert is_valid("((1 + 2) * 3) / 4 = 1.5") == True

def test_invalid_input_with_eval_complex():
    assert is_valid("(3 + 4) * 2 =") == False

def test_valid_input_with_eval_edge():
    assert is_valid("5 + 2 - 3 * 4 / 2 = 5") == True

def test_valid_input_with_eval_numbers():
    assert is_valid("1234567890") == True

def test_valid_input_with_eval_mixed():
    assert is_valid("1 + 2 * 3 - 4 / 2 = 5") == True

def test_invalid_input_with_eval_special_characters():
    assert is_valid("@ $ #") == False

def test_invalid_input_with_eval_starting_operator():
    assert is_valid("+ 3 * 5 = 15") == False

def test_valid_input_with_eval_function_call():
    assert is_valid("abs(-5)") == False
