import random
from chess import Move
import chess
from chess_engine.models.base import InitPlayer, AI

class MinMaxAI(AI): 
    def __init__(self, player: InitPlayer, heuristic, depth: int = 3) -> None:
        super().__init__(player)
        self.depth = depth
        self.heuristic = heuristic

    def makeMove(self, board: chess.Board) -> Move:
        moves = list(board.legal_moves)
        if len(moves) == 0:
            raise Exception("there are no moves")
        if len(moves) == 1:
            return moves[0]
        best_move = None
        best_v = float('-inf')
        
        for move in moves:
            n_p = board.copy()
            n_p.push(move)
            v =self.minmax(n_p,self.heuristic, False, self.depth-1)
            if v > best_v:
                best_v = v
                best_move = move
        
        return best_move
        
    def __str__(self) -> str:
        return "[name: {}, class: MinMaxAI]".format(self.name)
    def minmax(self, position, heuristic, player, depth):
        if position.is_game_over():
            if position.is_checkmate():
                return 0
            else:
                return float('inf') if not player else float('-inf')
        if depth == 0:
            return heuristic(position)
        
        moves = list(position.legal_moves)
        
        if player:
            v= float('-inf')
            for move in moves:
                n_p = position.copy()
                n_p.push(move)
                v= max(self.minmax(n_p,heuristic, not player, depth-1),v)
            return v 
        else :
            v= float('inf')
            for move in moves:
                n_p = position.copy()
                n_p.push(move)
                v = min(self.minmax(n_p,heuristic, not player, depth-1),v)
            return v