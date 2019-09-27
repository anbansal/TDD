import pytest
from pytest import raises
from unittest.mock import MagicMock
from LineReader import readFromFile


def test_returnsCorrectString(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="test line")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    result = readFromFile("check")
    mock_open.assert_called_once_with("check", "r")
    assert result == "test line"
