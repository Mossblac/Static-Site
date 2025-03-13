import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html(self):
        node2 = LeafNode("a", "Click me!", {"href": "http://www.google.com"})
        self.assertEqual(node2.to_html(), '<a href="http://www.google.com">Click me!</a>')

    def test_to_html(self):
        node3 = LeafNode(None, "testing", None)
        self.assertEqual(node3.to_html(), "testing")


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span></div>"
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_to_html_with_empty_children(self):
        child_node = LeafNode("", "")
        parent_node = ParentNode("a", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<a><></></a>"
        )
    def test_to_html_for_missing_tag(self):
        child_node = LeafNode("c", "what?")
        parent_node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_for_missing_child(self):
        child_node = LeafNode(None, None)
        parent_node = ParentNode("d", [child_node])
        with self.assertRaises(ValueError):
            parent_node.to_html()

    def test_to_html_with_props(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node], {"class": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div class="container"><span>child</span></div>'
        )
        
    def test_to_html_with_multiple_children(self):
        child1 = LeafNode("b", "bold")
        child2 = LeafNode("i", "italic")
        parent_node = ParentNode("p", [child1, child2])
        self


if __name__ == "__main__":
    unittest.main()