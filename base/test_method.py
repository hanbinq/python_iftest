import unittest
from demo import RunMain



class TestMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()

    def test_01(self):
        url = "http://106.75.9.19:88/topic/topic_list"
        data = {
            'page': 2,
            'pagesize': 3
        }
        res = self.run.run_main(url, 'POST',data)
        print(res)


if __name__ == '__main__':
    unittest.main()

