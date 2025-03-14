from textnode import TextType, TextNode



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

               


























if __name__ == "__main__":
    main()