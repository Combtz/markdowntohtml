import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
       node = HTMLNode("a", "Test HTMLNode with props", None, {"href" : "https://www.google.com", "target" : "_blank"})

       self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

    def test_htmlnode_repr(self):
        node = HTMLNode("div", "Test Node", None, None)
        node2 = HTMLNode("p", "Test HTMLNode Paragraph", [node], {"href" : "https://www.google.com", "target" : "_blank"})

        self.assertEqual(repr(node2), "HTMLNode(p, Test HTMLNode Paragraph, [HTMLNode(div, Test Node, None, None)], {'href': 'https://www.google.com', 'target': '_blank'})")

class TestLeafNode(unittest.TestCase):
    def test_leaf_node_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")
        self.assertEqual(node2.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    def test_leaf_node_repr(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

        self.assertEqual(repr(node), "LeafNode(p, This is a paragraph of text., None)")
        self.assertEqual(repr(node2), "LeafNode(a, Click me!, {'href': 'https://www.google.com'})")
       

if __name__ == "__main__":
    unittest.main()