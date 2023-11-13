from App import app
import atexit


def init():
    app.welcome()
    atexit.register(app.onquit)


if __name__ == "__main__":
    init()
    app.main()
