class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []

        self.props = props if props is not None else {}
        
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        result = " ".join(f'{key}="{value}"' for key, value in self.props.items())
        return f" {result}" if result else ""
    
    def __repr__(self):
        return f"HTMLNode(tag = {self.tag!r} value = {self.value!r} children = {self.children!r}, props = {self.props!r})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, props: dict = None):
        if value is None:
            raise ValueError("A value is required for a LeafNode")
        
        children = None

        super().__init__(tag, value, children=None, props = props)
        
    def to_html(self):
        if self.tag is None: return self.value

        if self.props:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        else:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None):
        if children is None:
            raise ValueError("ParentNode must contain children")
        if tag is None:
            raise ValueError("ParentNode must contain tag")

        super().__init__(tag, value = None, children = children, props = props)

    def to_html(self):
        if self.children is None:
            raise ValueError("ParentNode must contain children")
        if self.tag is None:
            raise ValueError("ParentNode must contain tag")
            
        result = f"<{self.tag}>"

        for child in self.children:
            result = result + child.to_html()
        return result + f"</{self.tag}>"
