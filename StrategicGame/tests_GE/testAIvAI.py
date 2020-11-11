import importlib
gameengine = importlib.import_module("Game-engine")
import unittest
import shutil
import json
from time import perf_counter

class TestAIvAI(unittest.TestCase):
    def countStones(self, board, player):
        count = 0
        for x in board:
            count = count + (1 if x == player else 0)
        return count
    
    def cantMove(self, board, player):
        adj = [(1,8,7), (0,9,2), (1,10,3), (2,4,11), (3,5,12), (4,6,13), (5,7,14), (0,6,15),
               (0,9,15,16), (1,8,10,17), (2,9,11,18), (3,12,12,19), (4,11,13,20), (5,12,14,21), (6,13,15,22), (7,8,14,23),
               (8,17,23), (9,16,18), (10,17,19), (11,18,20), (12,19,21), (13,20,22), (14,21,23), (15,16,22)]
        for pos in range (0,23):
            for x in adj[pos]:
                if board[x] == -1:
                    return False
        return True
    
    def changeAI(self, filename, difficulty):
        (board, player, turn, _) = gameengine.readInputFile(filename)
        gameengine.writeOutputFile(filename, board, player, turn, difficulty)

    def checkGameOver(self, filename):
        with open(filename) as f:
            data = json.load(f)
        board = list(data['Board'].values())
        if data['Turn'] < 18:
            return -1
        if self.countStones(board, 0) < 2:
            return 0
        if self.countStones(board, 1) < 2:
            return 1
        if self.cantMove(board, 0):
            return 0
        if self.cantMove(board, 1):
            return 1
        return -1

    def nextTurn(self, filename, ai):
        self.changeAI(filename, ai)
        gameengine.RunUUGame(ai)
        return self.checkGameOver(filename)

    def setUp(self):
        self.start_file = "test_aivai.json"
        self.test_file = "test_aivai_start.json"
        self.easy = 0
        self.medium = 1
        self.hard = 2
        self.maxtime = 5.0 * 60.0

    def runGame(self, ais):
        player = 0
        turn = 0
        shutil.copyfile(self.start_file, self.test_file)
        while turn < 200:
            self.changeAI(self.test_file, ais[player])
            start_time = perf_counter()
            gameengine.RunUUGame(self.test_file)
            stop_time = perf_counter()
            self.assertLess(stop_time - start_time, self.maxtime)
            loser = self.checkGameOver(self.test_file)
            if loser != -1:
                return loser
            player = 1 - player
            turn = turn + 1
        return -1

    def testHardVSMedium(self):
        loser_hardvsmed = self.runGame([self.hard, self.medium])
        self.assertEqual(loser_hardvsmed, 0)
        loser_medvshard = self.runGame([self.medium, self.hard])
        self.assertEqual(loser_medvshard, 1)
    
    def testHardVSEasy(self):
        loser_hardvseasy = self.runGame([self.hard, self.easy])
        self.assertEqual(loser_hardvseasy, 0)
        loser_easyvshard = self.runGame([self.easy, self.hard])
        self.assertEqual(loser_easyvshard, 1)
        
    def testMediumVSEasy(self):
        loser_medvseasy = self.runGame([self.medium, self.easy])
        self.assertEqual(loser_medvseasy, 0)
        loser_easyvsmed = self.runGame([self.easy, self.medium])
        self.assertEqual(loser_easyvsmed, 1)

if __name__ == '__main__':
    unittest.main()