from Bot import Bot
from GameAction import GameAction
from GameState import GameState
import numpy as np

class MinimaxBot(Bot):
    def get_action(self, state: GameState) -> GameAction:
        # Return the best action for the current state with minimax algorithm.
        # You can use the following functions:
        #   - self.get_successors(state)
        #   - self.is_terminal(state)
        #   - self.evaluate(state)
        #   - self.get_player_id(state)

        depth = np.len(state.row_status == 1 or state.col_status == 1)
        return self.minimax(state, depth)

    def minimax(self, state: GameState, depth: int, maximizingPlayer: bool):
        if depth == 0 or self.is_terminal(state):
            return self.evaluate(state)

        if maximizingPlayer:
            bestValue = -np.inf
            for child in self.get_successors(state):
                value = self.minimax(child, depth - 1, False)
                bestValue = max(bestValue, value)
            return bestValue
        else:
            bestValue = np.inf
            for child in self.get_successors(state):
                value = self.minimax(child, depth - 1, True)
                bestValue = min(bestValue, value)
            return bestValue

    def get_successors(self, state: GameState) -> list[GameState]:
        # Return a list of all successor states of the given state.

        successors = []
        
        

        