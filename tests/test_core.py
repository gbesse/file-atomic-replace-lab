import unittest
from file_atomic_replace_lab.core import run
class DomainTests(unittest.TestCase):
 def test_crash_boundaries(self):
  x=run({})['receipts'];self.assertEqual([r['content']for r in x],['OLD_COMPLETE','NEW_COMPLETE']);self.assertTrue(x[0]['temp_remains']);self.assertFalse(x[1]['temp_remains']);self.assertTrue(all(r['exit_code']<0 for r in x))
