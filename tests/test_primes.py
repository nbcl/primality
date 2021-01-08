import unittest

from primality import primality
from primality.random_strategy import RandomStrategy


class PrimalityTests(unittest.TestCase):

    def test_correct_prime(self):
        is_prime = primality.isprime(32424781)
        self.assertEqual(is_prime, True)

    def test_incorrect_prime(self):
        not_prime = primality.isprime(32424581)
        self.assertEqual(not_prime, False)

    def test_between_center(self):
        between_primes = primality.between(1000, 2000)
        test_result = [1009, 1013, 1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061,
                       1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123,
                       1129, 1151, 1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213,
                       1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283,
                       1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361,
                       1367, 1373, 1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439,
                       1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493,
                       1499, 1511, 1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571,
                       1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627,
                       1637, 1657, 1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721,
                       1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789,
                       1801, 1811, 1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877,
                       1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973,
                       1979, 1987, 1993, 1997, 1999]
        self.assertEqual(between_primes, test_result)

    def test_between_start(self):
        between_primes = primality.between(0, 50)
        test_result = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        self.assertEqual(between_primes, test_result)

    def test_nth_prime(self):
        millionth_prime = primality.nthprime(9999)
        self.assertEqual(millionth_prime, 104729)

    def test_next_prime(self):
        next_prime = primality.nextprime(15485863)
        self.assertEqual(next_prime, 15485867)

    def test_previous_prime(self):
        previous_prime = primality.prevprime(15485867)
        self.assertEqual(previous_prime, 15485863)

    def test_prange(self):
        prime_range = primality.prange(10)
        expected_result = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        self.assertEqual(prime_range, expected_result)

    def test_rand_primes_random_lib(self):
        lower_bound = 10
        upper_bound = 200

        for i in range(10):
            for strategy in RandomStrategy:
                random_prime = primality.rand_prime(lower_bound, upper_bound, strategy)
                self.assertTrue(primality.isprime(random_prime))
                self.assertGreater(random_prime, lower_bound)
                self.assertLess(random_prime, upper_bound)


if __name__ == '__main__':
    unittest.main()
