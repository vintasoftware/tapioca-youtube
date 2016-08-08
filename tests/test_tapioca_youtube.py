# coding: utf-8

import unittest

from tapioca_youtube import Youtube


class TestTapiocaYoutube(unittest.TestCase):

    def setUp(self):
        self.wrapper = Youtube()


if __name__ == '__main__':
    unittest.main()
