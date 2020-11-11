import importlib
gameengine = importlib.import_module("Game-engine")
import unittest

class TestAdjacentLocations(unittest.TestCase):
    def setUp(self):
        self.corner = 2
        self.out_corner = [1,10,3]
        self.horiz = 15
        self.out_horiz = [8,23,14,7]
        self.vert = 9
        self.out_vert = [8,1,10,17]
        self.diag = 20
        self.out_diag = [21,19,12]
    
    def testcases(self):
        test_corner = gameengine.adjacentLocations(self.corner)
        self.assertEqual(set(test_corner), set(self.out_corner))
        test_horiz = gameengine.adjacentLocations(self.horiz)
        self.assertEqual(set(test_horiz), set(self.out_horiz))
        test_vert = gameengine.adjacentLocations(self.vert)
        self.assertEqual(set(test_vert), set(self.out_vert))
        test_diag = gameengine.adjacentLocations(self.diag)
        self.assertEqual(set(test_diag), set(self.out_diag))

if __name__ == '__main__':
    unittest.main()