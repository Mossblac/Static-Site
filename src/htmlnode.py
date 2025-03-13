

class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):

        self.tag = tag
        self.value = value 
        self.children = children 
        self.props = props


    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if not self.props:
            return ""
        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'
        return props_str

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("missing tag value")
        if self.children is None:
            raise ValueError("missing children value")
        result = f'<{self.tag}'
        if self.props:
            props_str = self.props_to_html()
            result += props_str
        result += '>'
        for child in self.children:
            result += child.to_html()
        result += f"</{self.tag}>"
        return result

        
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, children=None, props=props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError
        if self.tag is None:
            return f"{self.value}"
        if self.props:
            props_str = self.props_to_html()
            return f"<{self.tag}{props_str}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
    


        