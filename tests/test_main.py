from pytest import CaptureFixture

from python_starter import main


def test_myoutput(capsys: CaptureFixture[str]) -> None:  # or use "capfd" for fd-level
    main()
    captured = capsys.readouterr()
    assert captured.out == (
        "Welcome to python_starter!\n" + "the helper value is: 42\n"
    )
