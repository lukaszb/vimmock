"""
vim mock object for easier testing of vim plugins written in Python.
"""
import sys
from vimmock.mocked import VimMock

VERSION = (0, 1, 1)

__all__ = ['VimMock']
__version__ = '.'.join((str(each) for each in VERSION[:4]))


def get_version():
    """
    Returns shorter version (digit parts only) as string.
    """
    return '.'.join((str(each) for each in VERSION[:4]))


def patch_vim():
    """
    Sets new ``VimMock`` instance under ``vim`` key within ``sys.modules``.
    """
    sys.modules['vim'] = VimMock()

