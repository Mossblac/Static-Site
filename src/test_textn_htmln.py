import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
from text_node_to_html_node import text_node_to_html_node



class TestMain(unittest.TestCase):
    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_bold(self):
        node1 = TextNode("this is bold", TextType.BOLD)
        html_node1 = text_node_to_html_node(node1)
        self.assertEqual(html_node1.tag, "b")
        self.assertEqual(html_node1.value, "this is bold")
        
    def test_exception(self):
        node = TextNode("some text", "highlight")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)
            
    def test_italic(self):
        node = TextNode("this is italic", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "this is italic")

    def test_code(self):
        node = TextNode("this is code", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "this is code")

    def test_link(self):
        node = TextNode("click me", TextType.LINK, "http//:www.google.com")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "click me")
        self.assertEqual(html_node.props, {'href':"http//:www.google.com"})

    def test_image(self):
        node = TextNode("alt text", TextType.IMAGE, "/image.jpeg")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.value, "")
        self.assertEqual(html_node.props, {"src": "/image.jpeg", "alt": "alt text"})
    








if __name__ == "__main__":
    unittest.main()