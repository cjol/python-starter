from pytest import CaptureFixture

from cls_finance import main


def test_myoutput(capsys: CaptureFixture[str]) -> None:  # or use "capfd" for fd-level
    main()
    captured = capsys.readouterr()
    assert captured.out == (
        "Welcome to cls_finance!\n" + "the helper value is: 42\n"
    )
