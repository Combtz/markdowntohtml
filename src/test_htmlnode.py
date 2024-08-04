import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
       node = HTMLNode("a", "Test HTMLNode with props", None, {"href" : "https://www.google.com", "target" : "_blank"})

       self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\" target=\"_blank\"")

    def test_htmlnode_repr(self):
        node = HTMLNode("div", "Test Node", None, None)
        node2 = HTMLNode("p", "Test HTMLNode Paragraph", [node], {"href" : "https://www.google.com", "target" : "_blank"})

        self.assertEqual(repr(node2), "HTMLNode(p, Test HTMLNode Paragraph, [HTMLNode(div, Test Node, None, None)], {'href': 'https://www.google.com', 'target': '_blank'})")

if __name__ == "__main__":
    unittest.main()