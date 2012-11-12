try:
    import unittest2 as unittest
except ImportError:
    import unittest

from mock import Mock
from vimmock.mocked import BufferMock
from vimmock.mocked import CurrentMock
from vimmock.mocked import LineMock
from vimmock.mocked import RangeMock
from vimmock.mocked import VimMock
from vimmock.mocked import WindowMock
import sys
import vimmock


class TestVimMock(unittest.TestCase):

    def setUp(self):
        self.vim = VimMock()

    def test_init(self):
        self.assertTrue(isinstance(self.vim.current, CurrentMock))

    def test_setup_text(self):
        self.vim.current.buffer = Mock()
        self.vim.setup_text('foobar')
        self.vim.current.buffer.setup_text.assert_called_once_with('foobar')


class TestBufferMock(unittest.TestCase):

    def setUp(self):
        self.buffer = BufferMock('foo\nbar\nbaz')

    def test_getitem(self):
        self.assertEqual(self.buffer[0], 'foo')
        self.assertEqual(self.buffer[1], 'bar')
        self.assertEqual(self.buffer[2], 'baz')
        self.assertEqual(self.buffer[-1], 'baz')

        with self.assertRaises(TypeError):
            self.buffer['1']

    def test_getitem_range(self):
        self.assertEqual(self.buffer[:1], ['foo'])
        self.assertEqual(self.buffer[1:5], ['bar', 'baz'])

    def test_setitem(self):
        self.buffer[0] = 'new foo'
        self.assertEqual(self.buffer[0], 'new foo')
        self.assertEqual(self.buffer[1], 'bar')

        with self.assertRaises(TypeError):
            self.buffer['1'] = 'foo'

    def test_setitem_range(self):
        self.buffer[:2] = ['aaa', 'bbb']
        self.assertEqual(self.buffer[:2], ['aaa', 'bbb'])

    def test_setup_text(self):
        self.buffer.setup_text('\n'.join(('foo', 'bar')))

class TestCurrentMock(unittest.TestCase):

    def setUp(self):
        self.current = CurrentMock()

    def test_init(self):
        self.assertTrue(isinstance(self.current.buffer, BufferMock))
        self.assertTrue(isinstance(self.current.line, LineMock))
        self.assertTrue(isinstance(self.current.window, WindowMock))
        self.assertTrue(isinstance(self.current.range, RangeMock))


class TestPatch(unittest.TestCase):

    def test_patch_vim(self):
        sys.modules['vim'] = object()

        vimmock.patch_vim()
        self.assertIsInstance(sys.modules['vim'], VimMock)


if __name__ == '__main__':
    unittest.main()

