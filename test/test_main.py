import sys
import pytest

import main


def test_importable():
    # importing the module should not execute CLI logic
    assert hasattr(main, "main")


def test_version_flag(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["mvld", "--version"])
    with pytest.raises(SystemExit):
        main.main()
    captured = capsys.readouterr()
    assert "1.2.0" in captured.out
