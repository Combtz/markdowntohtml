# A class that presents one node of a html documenty tree
class HTMLNode():
    def __init__(self, tag, value, children, props):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()
    
    # Returns props as in html syntax
    def props_to_html(self):
        if self.props == None:
            return ""

        props_html = " ".join(map(lambda kv: f"{kv[0]}=\"{kv[1]}\"", self.props.items()))

        return " " + props_html
    
    # String representation of html node
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
# A class that represents a single HTML tag with no children
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("Leafnode must have value")
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"