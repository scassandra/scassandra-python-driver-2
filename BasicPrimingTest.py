import unittest
import logging
from cassandra.cluster import Cluster


class BasicPrimingTest(unittest.TestCase):

    def testUseAndSimpleQueryWithNoPrime(self):
        logging.basicConfig(level=logging.DEBUG)
        cluster = Cluster(['127.0.0.1'],port=8042)
        keyspace = cluster.connect("people")

        keyspace.execute("anykeyspace")
        rows = keyspace.execute("select * from people")
        self.assertEqual(len(list(rows)), 0)
