# Imports
import sys
import hyperdex.admin
import testlib
assertEquals = testlib.assertEquals
assertTrue = testlib.assertTrue
assertFalse = testlib.assertFalse

# Setup
a = hyperdex.admin.Admin(sys.argv[1], int(sys.argv[2]))

# Test Add/Remove
assertEquals(a.list_spaces(), [])
assertTrue(a.add_space('space test1 key key1 attributes a1, a2'))
assertEquals(a.list_spaces(), ['test1'])
assertTrue(a.add_space('space test2 key key1 attributes a1, a2'))
assertTrue(a.add_space('space test3 key key1 attributes a1, a2'))
assertEquals(a.list_spaces(), ['test1', 'test2', 'test3'])
assertTrue(a.rm_space('test2'))
assertEquals(a.list_spaces(), ['test1', 'test3'])
#FIXME find a way to test exceptions
#assertFalse(a.rm_space('test5'))
#assertEquals(a.list_spaces(), ['test1', 'test3'])
assertTrue(a.rm_space('test1'))
assertTrue(a.rm_space('test3'))
assertEquals(a.list_spaces(), [])

# Test Indexing
assertTrue(a.add_space('space test1 key key1 attributes a1, a2'))
assertTrue(a.add_index('test1', 'a1'))
#TODO no way to list indexes
assertTrue(a.rm_index('test1', 'a1'))
assertTrue(a.rm_space('test1'))
