import unittest

from htmlnode import HTMLNode, LeafNode


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

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!", props=None)
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html(self):
        node2 = LeafNode("a", "Click me!", {"href": "http://www.google.com"})
        self.assertEqual(node2.to_html(), '<a href="http://www.google.com">Click me!</a>')

    def test_to_html(self):
        node3 = LeafNode(None, "testing", None)
        self.assertEqual(node3.to_html(), "testing")

    

if __name__ == "__main__":
    unittest.main()