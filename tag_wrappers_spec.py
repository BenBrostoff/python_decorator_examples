import unittest
from tag_wrappers import *

class TestWrapperFunctions(unittest.TestCase):
  

  def test_func_equality(self):  
    example_text = 'Example'
    self.assertEqual(non_dec_p_wrapper(example_text),
                     dec_p_wrapper(example_text))
    self.assertEqual(non_dec_div_wrapper(example_text),
                     dec_div_wrapper(example_text))

  def test_dynamic_wrapper(self):
    example_text = 'Example'
    self.assertEqual(dynamic_wrapper('div', example_text),
                     '<div>Example</div>')
    self.assertEqual(dynamic_wrapper('p', example_text),
                     '<p>Example</p>')


if __name__ == '__main__':
    unittest.main()