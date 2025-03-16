import unittest
from textnode import TextNode, TextType
from htmlnode import HTMLNode, ParentNode, LeafNode
from split_code import split_nodes_delimiter


class Test_Split_Code(unittest.TestCase):
    def test_delimeter(self):
        node = TextNode("This is a sentence with a **bold** word in it", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_node, [
            TextNode("This is a sentence with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word in it", TextType.TEXT)

        ])

    def test_multiple_del(self):
        node = TextNode("multiple _words_ are very _italic_ in this sentence", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_node, [
            TextNode("multiple ", TextType.TEXT),
            TextNode("words", TextType.ITALIC),
            TextNode(" are very ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" in this sentence", TextType.TEXT)

        ])

    def test_recursion(self):
        node = TextNode("this `text` is `actually` very `annoying` to `test`", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_node, [
            TextNode("this ", TextType.TEXT),
            TextNode("text", TextType.CODE),
            TextNode(" is ", TextType.TEXT),
            TextNode("actually", TextType.CODE), 
            TextNode(" very ", TextType.TEXT),
            TextNode("annoying", TextType.CODE),
            TextNode(" to ", TextType.TEXT),
            TextNode("test", TextType.CODE)

        ])


    def test_no_close_error(self):
        node = TextNode("this **bold is missing something", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_one_line(self):
        node = TextNode("_saucy_", TextType.TEXT)
        new_node = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_node, [TextNode("saucy", TextType.ITALIC)])

if __name__ == "__main__":
    unittest.main()