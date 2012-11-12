
vimmock
=======

.. image:: https://secure.travis-ci.org/lukaszb/vimmock.png?branch=master
  :target: http://travis-ci.org/lukaszb/vimmock

vimmock is a module that makes testing Python code using *vim* module much
easier.


Usage
=====

At the test environment initialization one should prepare ``vim`` object that
would normaly be used within vim's plugin. We have added convenient function for
that::

    import vimmock
    vimmock.patch_vim()

This is equivalent to::

    import sys
    from vimmock import VimMock

    sys.modules['vim'] = VimMock()

Once this is done one can start importing *vim* module which would be instance
of *VimMock* class. From now on we can write our tests (and import ``vim``
module)::

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


Work in progress
----------------

Please note that ``vimmock`` is a work-in-progress module. Only basic mocks are
actually completed. If you want to use this module for now it is best if you
fork it, link to your ``PYTHONPATH`` environment variable and modify on the fly.
Pull requests are welcome!

