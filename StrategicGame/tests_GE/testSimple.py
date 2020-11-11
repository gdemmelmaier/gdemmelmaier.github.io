import importlib
gameengine = importlib.import_module("Game-engine")
import unittest
import shutil
import json

def cmp(a, b):
    return (a > b) - (a < b) 

class TestSimple(unittest.TestCase):
    def generateBoard(self, indices):
        board = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        for x in indices:
            board[x[0]] = x[1]
        return board
    
    def countStones(self, board, player):
        count = 0
        for x in board:
            count = count + (1 if x == player else 0)
        return count
    
    def countMills(self, board, player):
        count = 0
        mill_positions = [(0,1,2),(8,9,10),(16,17,18),(7,15,23),(19,11,3),(22,21,20),(14,13,12),(6,5,4),
                          (0,7,6),(8,15,14),(16,23,22),(1,9,7),(21,13,5),(18,19,20),(10,11,12),(2,3,4),
                          (0,8,16),(2,10,18),(6,14,22),(4,12,20)]
        for x in mill_positions:
            count = count + (1 if x[0] == player and x[1] == player and x[2] == player else 0)
        return count
    
    def readFile(self, filename):
        with open(filename) as f:
            data = json.load(f)
        return (list(data['Board'].values()), data['Player'])

    def setUp(self):
        self.test_file = "test.json"
        self.board_invalid_key = "board_invalid_key.json"
        self.board_invalid_value = "board_invalid_value.json"
        self.board_not_ascending = "board_not_ascending.json"
        self.board_too_long = "board_too_long.json"
        self.board_too_short = "board_too_short.json"
        self.difficulty_invalid = "difficulty_invalid.json"
        self.player_invalid = "player_invalid.json"
        self.turn_invalid = "turn_invalid.json"
        self.valid_input = "placeholder"

        self.board_mill_d = self.generateBoard([(0,0),(8,0),(16,0), (6,1),(4,1),(2,1)])
        self.board_mill_h = self.generateBoard([(16,1),(17,1),(18,1), (6,0),(4,0),(2,0)])
        self.board_mill_v = self.generateBoard([(2,0),(3,0),(4,0), (0,0),(6,0),(23,0)])
        self.board_halfmill_d = self.generateBoard([(22,0),(19,0),(20,0), (0,1),(2,1),(4,1)])
        self.board_halfmill_h = self.generateBoard([(11,1),(3,1),(5,1), (0,0),(16,0),(20,0)])
        self.board_halfmill_v = self.generateBoard([(16,1),(23,1),(19,1), (0,0),(2,0),(4,0)])
        self.board_3pc_1 = self.generateBoard([(23,1),(22,1),(21,1), (0,0),(2,0),(4,0)])
        self.board_3pc_2 = self.generateBoard([(6,0),(14,0),(5,0), (0,1),(2,1),(4,1)])
        self.board_3pc_3 = self.generateBoard([(9,0),(10,0),(18,0), (0,1),(6,1),(4,1)])
        self.board_finished_game1 = self.generateBoard([(0,0),(11,0),(19,0),(17,0),(15,1),(3,1)])
        self.board_finished_game2 = self.generateBoard([(15,0),(23,0),(22,0),(14,0), (8,1),(16,1),(7,1),(6,1),(13,1),(21,1)])
        self.board_no_features = self.generateBoard([(0,0),(6,0),(4,0), (2,1),(16,1),(20,1)])

        self.remove_stone_mill = "test_remove_stone_mill.json"
        self.remove_stone_no_mill = "test_remove_stone_no_mill.json"
    
    def testInvalidInputFile(self):
        shutil.copyfile(self.board_invalid_key, self.test_file)
        self.assertRaises(ValueError, gameengine.RunUUGame, self.test_file)
        shutil.copyfile(self.board_invalid_value, self.test_file)
        self.assertRaises(ValueError, gameengine.RunUUGame, self.test_file)
        shutil.copyfile(self.board_not_ascending, self.test_file)
        self.assertRaises(ValueError, gameengine.RunUUGame, self.test_file)
        shutil.copyfile(self.board_too_long, self.test_file)
        self.assertRaises(ValueError, gameengine.RunUUGame, self.test_file)
        shutil.copyfile(self.board_too_short, self.test_file)
        self.assertRaises(ValueError, gameengine.RunUUGame, self.test_file)
        shutil.copyfile(self.difficulty_invalid, self.test_file)
        self.assertRaises(ValueError, gameengine.RunUUGame, self.test_file)
        shutil.copyfile(self.player_invalid, self.test_file)
        self.assertRaises(ValueError, gameengine.RunUUGame, self.test_file)
        shutil.copyfile(self.turn_invalid, self.test_file)
        self.assertRaises(ValueError, gameengine.RunUUGame, self.test_file)
        shutil.copyfile(self.valid_input, self.test_file)
        try:
            runUUGame(self.test_file)
            self.assertTrue(True)
        except:
            self.assertTrue(False)
    
    def testFeaturesOfInterest(self):
        test_mill_h_p0 = gameengine.heuristic(self.board_mill_h, 0, 30)
        test_mill_h_p1 = gameengine.heuristic(self.board_mill_h, 1, 30)
        self.assertEqual(cmp(test_mill_h_p0,0) + cmp(test_mill_h_p1,0), 0)
        self.assertNotEqual(test_mill_h_p1, 0)
        
        test_mill_d_p0 = gameengine.heuristic(self.board_mill_d, 0, 30)
        test_mill_d_p1 = gameengine.heuristic(self.board_mill_d, 1, 30)
        self.assertEqual(cmp(test_mill_d_p0,0) + cmp(test_mill_d_p1,0), 0)
        self.assertNotEqual(test_mill_d_p1, 0)
        
        test_mill_v_p0 = gameengine.heuristic(self.board_mill_v, 0, 30)
        test_mill_v_p1 = gameengine.heuristic(self.board_mill_v, 1, 30)
        self.assertEqual(cmp(test_mill_v_p0,0) + cmp(test_mill_v_p1,0), 0)
        self.assertNotEqual(test_mill_v_p1, 0)
        
        test_halfmill_h_p0 = gameengine.heuristic(self.board_halfmill_h, 0, 30)
        test_halfmill_h_p1 = gameengine.heuristic(self.board_halfmill_h, 1, 30)
        self.assertEqual(cmp(test_halfmill_h_p0,0) + cmp(test_halfmill_h_p1,0), 0)
        self.assertNotEqual(test_halfmill_h_p1, 0)
        
        test_halfmill_d_p0 = gameengine.heuristic(self.board_halfmill_d, 0, 30)
        test_halfmill_d_p1 = gameengine.heuristic(self.board_halfmill_d, 1, 30)
        self.assertEqual(cmp(test_halfmill_d_p0,0) + cmp(test_halfmill_d_p1,0), 0)
        self.assertNotEqual(test_halfmill_d_p1, 0)
        
        test_halfmill_v_p0 = gameengine.heuristic(self.board_halfmill_v, 0, 30)
        test_halfmill_v_p1 = gameengine.heuristic(self.board_halfmill_v, 1, 30)
        self.assertEqual(cmp(test_halfmill_v_p0,0) + cmp(test_halfmill_v_p1,0), 0)
        self.assertNotEqual(test_halfmill_v_p1, 0)
        
        test_3pc_1_p0 = gameengine.heuristic(self.board_3pc_1, 0, 30)
        test_3pc_1_p1 = gameengine.heuristic(self.board_3pc_1, 1, 30)
        self.assertEqual(cmp(test_3pc_1_p0,0) + cmp(test_3pc_1_p1,0), 0)
        self.assertNotEqual(test_3pc_1_p1, 0)
        
        test_3pc_2_p0 = gameengine.heuristic(self.board_3pc_2, 0, 30)
        test_3pc_2_p1 = gameengine.heuristic(self.board_3pc_2, 1, 30)
        self.assertEqual(cmp(test_3pc_2_p0,0) + cmp(test_3pc_2_p1,0), 0)
        self.assertNotEqual(test_3pc_2_p1, 0)
        
        test_3pc_3_p0 = gameengine.heuristic(self.board_3pc_3, 0, 30)
        test_3pc_3_p1 = gameengine.heuristic(self.board_3pc_3, 1, 30)
        self.assertEqual(cmp(test_3pc_3_p0,0) + cmp(test_3pc_3_p1,0), 0)
        self.assertNotEqual(test_3pc_3_p1, 0)
        
        test_finished_game1_p0 = gameengine.heuristic(self.board_finished_game1, 0, 30)
        test_finished_game1_p1 = gameengine.heuristic(self.board_finished_game1, 1, 30)
        self.assertEqual(cmp(test_finished_game1_p0,0) + cmp(test_finished_game1_p1,0), 0)
        self.assertNotEqual(test_finished_game1_p1, 0)
    
        test_finished_game2_p0 = gameengine.heuristic(self.board_finished_game2, 0, 30)
        test_finished_game2_p1 = gameengine.heuristic(self.board_finished_game2, 1, 30)
        self.assertEqual(cmp(test_finished_game2_p0,0) + cmp(test_finished_game2_p1,0), 0)
        self.assertNotEqual(test_finished_game2_p1, 0)

        test_no_features_p0 = gameengine.heuristic(self.board_no_features, 0, 30)
        test_no_features_p1 = gameengine.heuristic(self.board_no_features, 1, 30)
        self.assertEqual(test_no_features_p0, 0)
        self.assertEqual(test_no_features_p1, 0)
    
    def testRemoveStoneMill(self):
        shutil.copyfile(self.remove_stone_mill, self.test_file)
        data = self.readFile(self.test_file)
        stones_p1_before = self.countStones(data[0], data[1])
        stones_p2_before = self.countStones(data[0], 1 - data[1])
        mills_p1_before = self.countMills(data[0], data[1])
        mills_p2_before = self.countMills(data[0], 1 - data[1])
        gameengine.runUUGame(self.test_file)
        data = self.readFile(self.test_file)
        stones_p1_after = self.countStones(data[0], data[1])
        stones_p2_after = self.countStones(data[0], 1 - data[1])
        mills_p1_after = self.countMills(data[0], data[1])
        mills_p2_after = self.countMills(data[0], 1 - data[1])

        self.assertEqual(stones_p1_after, stones_p1_before + 1)
        self.assertEqual(stones_p2_after, stones_p2_before - 1)
        self.assertEqual(mills_p1_after, mills_p1_before + 1)
        self.assertEqual(mills_p2_after, mills_p2_before)
        
    def testRemoveStoneNoMill(self):
        shutil.copyfile(self.remove_stone_no_mill, self.test_file)
        data = self.readFile(self.test_file)
        stones_p1_before = self.countStones(data[0], data[1])
        stones_p2_before = self.countStones(data[0], 1 - data[1])
        mills_p1_before = self.countMills(data[0], data[1])
        mills_p2_before = self.countMills(data[0], 1 - data[1])
        gameengine.runUUGame(self.test_file)
        data = self.readFile(self.test_file)
        stones_p1_after = self.countStones(data[0], data[1])
        stones_p2_after = self.countStones(data[0], 1 - data[1])
        mills_p1_after = self.countMills(data[0], data[1])
        mills_p2_after = self.countMills(data[0], 1 - data[1])

        self.assertEqual(stones_p1_after, stones_p1_before + 1)
        self.assertEqual(stones_p2_after, stones_p2_before - 1)
        self.assertEqual(mills_p1_after, mills_p1_before + 1)
        self.assertEqual(mills_p2_after, mills_p2_before)

if __name__ == '__main__':
    unittest.main()