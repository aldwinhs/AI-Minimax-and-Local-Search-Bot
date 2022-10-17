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