import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_eq(self):
        node3 = TextNode("these are the same", TextType.ITALIC, url=None)
        node4 = TextNode("these are the same", TextType.ITALIC, url=None)
        self.assertEqual(node3, node4)

    def test_eq(self):

        node5 = TextNode("not the same", TextType.BOLD, url=None)
        node6 = TextNode("not the same", TextType.ITALIC, url=None)
        self.assertNotEqual(node5, node6)
        
        


if __name__ == "__main__":
    unittest.main()