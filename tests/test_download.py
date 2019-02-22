import pytest

import project0
from project0 import main
from project0 import project0


def test_download_sanity():
    assert main.download() is not None
