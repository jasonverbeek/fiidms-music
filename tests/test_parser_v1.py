from unittest import TestCase

from fiidms.parser.v1 import parse, parser


class ParserV1Test(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.expected_result = dict(
            artist=['a'],
            album='b',
            title='c',
            youtube_id='d')

    def test_parse_line(self):
        self.assertEqual(
            self.expected_result,
            parse("a|b|c|d"))

    def test_parse_file(self):
        self.assertEqual(
            [self.expected_result],
            list(parser('=v1\r\na|b|c|d')))

    def test_multi_artist(self):
        self.assertEqual(
            dict(self.expected_result, **{'artist': ['a', 'e']}),
            parse("a,e|b|c|d"))

    def test_exceptions(self):
        self.assertRaises(ValueError, parser, 'v1\r\na|b|c|d')
        self.assertRaises(ValueError, parser, '=v2\r\na|b|c|d')

