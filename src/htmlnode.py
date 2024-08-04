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
        props_html = " ".join(map(lambda kv: f"{kv[0]}=\"{kv[1]}\"", self.props.items()))

        return " " + props_html
    
    # String representation of html node
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"