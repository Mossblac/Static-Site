import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        prop = {"fozzy": "waka, waka", "kermit": "the frog"}
        node = HTMLNode(props=prop)
        expected = ' fozzy="waka, waka" kermit="the frog"'
        self.assertEqual(node.props_to_html(), expected)

    def test__repr__(self):
        prop = {"fozzy": "waka, waka"}
        node = HTMLNode("p", "the text inside the paragraph", None, prop)
        
        repr_string = repr(node)
        
        self.assertIn("p", repr_string)
        self.assertIn("the text inside the paragraph", repr_string)
        self.assertIn("fozzy", repr_string)
        self.assertIn("waka, waka", repr_string)
    
    def test_to_html(self):
        self.assertRaises(expected_exception=NotImplementedError)


if __name__ == "__main__":
    unittest.main()