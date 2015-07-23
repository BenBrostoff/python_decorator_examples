import unittest
from tag_wrappers import *

class TestWrapperFunctions(unittest.TestCase):
  def setUp(self):
    self.example_text = 'Example'

  def test_func_equality(self):  
    self.assertEqual(non_dec_p_wrapper(self.example_text),
                     dec_p_wrapper(self.example_text))
    self.assertEqual(non_dec_div_wrapper(self.example_text),
                     dec_div_wrapper(self.example_text))

  def test_dynamic_wrapper(self):
    for tag in ['div', 'h1', 'h2', 'h3', 'p', 'strong']:
      self.assertEqual(dynamic_wrapper(tag, self.example_text),
                       '<{tag}>Example</{tag}>'.format(tag=tag))


if __name__ == '__main__':
    unittest.main()