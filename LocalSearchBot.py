from Bot import Bot
from GameAction import GameAction
from GameState import GameState
from Objective import Objective

import numpy as np


class LocalSearchBot(Bot):
    def get_action(self, state: GameState) -> GameAction:
        return self.local_search(state)

    def local_search(self, state: GameState):
        best_action = None
        best_value = -np.inf

        # Search for the best action
        for action in Objective.get_action_successors(state):
            value = self.evaluate(Objective.get_successor_state(GameState(
                state.board_status.copy(),
                state.row_status.copy(),
                state.col_status.copy(),
                state.player1_turn), action))

            if value > best_value:
                best_value = value
                best_action = action

        # Because player need to take turn so we need to choose the best action not current state

        # Reverse X and Y
        return GameAction(best_action.action_type, (best_action.position[1], best_action.position[0]))

    def evaluate(self, state: GameState) -> int:
        # Return the evaluation value of the given state.
        # The evaluation value is the number of boxes filled by the current player.

        return np.sum(state.board_status == self.get_player_id(state))

    def get_player_id(self, state: GameState) -> int:
        # Return the player id of the given state.
        # The player id is 1 or 2.

        if (state.player1_turn):
            return -4
        else:
            return 4
