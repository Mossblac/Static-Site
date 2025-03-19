import re
from enum import Enum
from textnode import TextType, TextNode
from regex_code import extract_markdown_images, extract_markdown_links

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"



def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes



def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            text = node.text
            if delimiter in text:
                start_index = text.find(delimiter)
                end_index = text.find(delimiter, start_index + len(delimiter))
                if end_index == -1:
                    raise Exception("No closing delimiter found")
                
                before_text = text[:start_index]
                
                between_text = text[start_index + len(delimiter):end_index]
            
                after_text = text[end_index + len(delimiter):]
                 
                if before_text:
                    new_nodes.append(TextNode(before_text, TextType.TEXT))
                new_nodes.append(TextNode(between_text, text_type))
                if after_text:
                    temp_node = TextNode(after_text, TextType.TEXT)
                    result = split_nodes_delimiter([temp_node], delimiter, text_type)
                    new_nodes.extend(result)
            else:
                new_nodes.append(node)
    
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def markdown_to_blocks(markdown):
    markdown_split = markdown.split("\n\n")
    markdown_block = []
    for line in markdown_split:
        markdown_block.append(line.strip())

    return markdown_block

def block_to_block_type(block):
    pass
#assignment it takes a block and returns a BlockType 
#Headings start with 1-6 # characters, followed by a space and then the heading text.
#Code blocks must start with 3 backticks and end with 3 backticks.
#Every line in a quote block must start with a > character.
#Every line in an unordered list block must start with a - character, followed by a space.
#Every line in an ordered list block must start with a number followed by a . character and a space. The number must start at 1 and increment by 1 for each line.
#If none of the above conditions are met, the block is a normal paragraph.


if __name__ == "__main__":
    main()