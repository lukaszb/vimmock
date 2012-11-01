
vimmock
=======

.. image:: https://secure.travis-ci.org/lukaszb/vimmock.png?branch=master
  :target: http://travis-ci.org/lukaszb/vimmock

vimmock is a module that makes testing Python code using *vim* module much
easier.


Usage
=====

At the test environment initialization one should prepare ``vim`` object that
would normaly be used within vim's plugin. Example::


    import sys
    from vimmock import VimMock

    sys.modules['vim'] = VimMock()

Once this is done one can start importing *vim* module which would be instance
of *VimMock* class. From now on we can write our tests::

    import vim
    import unittest
    import myplugin

    class TestPlugin(unittest.TestCase):
        
        def setUp(self):
            vim.setup_text('\n'.join(('foo', 'bar')))

        def test_simple(self):
            vim.current.window.cursor = 2, 0 # rows starts from 1, column from 0
            # ... let's assume our plugin swaps lines
            self.assertEqual(vim.current.buffer[0], 'bar')
            self.assertEqual(vim.current.buffer[1], 'foo')


Development
===========

Please use github's issue tracker for filing new issues. Preferred way of
attaching patches is via *pull requests*.

