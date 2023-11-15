from src.App import app

def test_welcome(capfd):
    app.welcome()
    out, _ = capfd.readouterr()
    assert "WELCOME TO COMMANDLINE CALCULATOR!!" in out
