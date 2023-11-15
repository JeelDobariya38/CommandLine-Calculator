from src.App.historytracker import History

def test_append_operation():
    history = History()
    history.append_operation("3 + 5", "8")
    history.append_operation("7 % 3 = 1", "1")
    assert history.history == ["3 + 5 -> 8", "7 % 3 = 1 -> 1"]

def test_repr_method():
    history = History()
    history.append_operation("3 + 5", "8")
    history.append_operation("7 % 3 = 1", "1")

    assert repr(history) == "3 + 5 -> 8\n7 % 3 = 1 -> 1\n"

def test_clear_history():
    history = History()
    history.append_operation("3 + 5", "8")
    history.append_operation("7 % 3 = 1", "1")

    history.clear_history()
    assert history.history == []
