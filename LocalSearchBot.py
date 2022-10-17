from Bot import Bot
from GameAction import GameAction
from GameState import GameState

import numpy as np

class LocalSearchBot(Bot):
    def get_action(self, state: GameState) -> GameAction:
        # Return the best action for the current state with local search algorithm.
        # You can use the following functions:
        #   - self.get_successors(state)
        #   - self.is_terminal(state)
        #   - self.evaluate(state)
        #   - self.get_player_id(state)

        return self.local_search(state)

    def local_search(self, state: GameState):
        best_action = None
        best_value = -np.inf
        for action in self.get_successors(state):
            value = self.evaluate(action)
            if value > best_value:
                best_value = value
                best_action = action

        return best_action

    def get_successors(self, state: GameState) -> list[GameState]:
        # Return a list of all successor states of the given state.

        successors = []
        
        for i in range(len(state.row_status)):
            for j in range(len(state.row_status[0])):
                if state.row_status[i][j] == 0:
                    successors.append(GameAction("row", (i, j)))

        for i in range(len(state.col_status)):
            for j in range(len(state.col_status[0])):
                if state.col_status[i][j] == 0:
                    successors.append(GameAction("col", (i, j)))

        return successors

    def evaluate(self, state: GameState) -> int:
        # Return the evaluation value of the given state.
        # The evaluation value is the number of boxes filled by the current player.



        return np.sum(state.board == self.get_player_id(state))

    def get_player_id(self, state: GameState) -> int:
        # Return the player id of the given state.
        # The player id is 1 or 2.

        if(state.player1_turn):
            return -4
        else:
            return 4