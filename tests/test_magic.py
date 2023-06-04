import pytest
from module import magic
import sys

skip_text = True

@pytest.mark.xfail
def test_get_a_number():
    result = magic.get_a_number()
    assert result == 36.1

@pytest.mark.skip
def test_get_a_double():
    result = magic.get_a_double(36)
    assert result == 72

@pytest.mark.skipif(skip_text == True, reason='just for testing')
def test_get_a_list():
    result = magic.get_a_list(1, 2, 3)
    assert result == [1, 2, 3]

@pytest.mark.skipif(sys.version_info < (3, 9), reason='python 3.10 version not found')
def test_get_a_string():
    result = magic.get_a_string()
    assert result == "dadapeer"