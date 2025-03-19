import unittest

from textnode import TextNode, TextType, text_node_to_html_node
from regex_code import extract_markdown_images, extract_markdown_links


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq(self):
        node3 = TextNode("these are the same", TextType.ITALIC, url=None)
        node4 = TextNode("these are the same", TextType.ITALIC, url=None)
        self.assertEqual(node3, node4)

    def test__repr__(self):
        node = TextNode("these are the same", TextType.ITALIC, url=None)

        repr_string = repr(node)
        self.assertIn("these are the same", repr_string)


class TestRegex(unittest.TestCase):     
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)


    def test_extract_markdown_altered_images(self):
        matches = extract_markdown_images(
        "This is (text) with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)



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