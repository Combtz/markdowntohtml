from mdtohtml import extract_title

import unittest

class TestExtractTitle(unittest.TestCase):

    def test_extract_title_with_h1(self):
        markdown = "# Hello World"
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_extract_title_with_whitespace(self):
        markdown = "#   Hello World   "
        self.assertEqual(extract_title(markdown), "Hello World")

    def test_extract_title_no_h1(self):
        markdown = "## Hello World"
        with self.assertRaises(ValueError):
            extract_title(markdown)

    def test_extract_title_multiple_h1(self):
        markdown = "# First Title\n# Second Title"
        self.assertEqual(extract_title(markdown), "First Title")

if __name__ == "__main__":
    unittest.main()
