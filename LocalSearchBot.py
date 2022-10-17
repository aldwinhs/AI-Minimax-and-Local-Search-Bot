from Bot import Bot
from GameAction import GameAction
from GameState import GameState

import numpy as np

class LocalSearchBot(Bot):
    def get_action(self, state: GameState) -> GameAction:
        print("LocalSearchBot is thinking...")
        # Return the best action for the current state with local search algorithm.
        # You can use the following functions:
        #   - self.get_successors(state)
        #   - self.is_terminal(state)
        #   - self.evaluate(state)
        #   - self.get_player_id(state)

        return self.local_search(state)

    def local_search(self, state: GameState):
        print("Local_search is thinking...")
        best_action = None
        best_value = -np.inf

        # Search for the best action
        for action in self.get_successors(state):
            value = self.evaluate(self.get_successor_state(GameState(
                state.board_status.copy(),
                state.row_status.copy(),
                state.col_status.copy(),
                state.player1_turn), action)) 
            
            if value > best_value:
                best_value = value
                best_action = action

        # Because player need to take turn so we need to choose the best action not current state

        return best_action

    def get_successors(self, state: GameState) -> list[GameAction]:
        # Return a list of all successor states of the given state.
        print("get_successors is thinking...")
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

    def get_successor_state(self, state: GameState, action: GameAction) -> GameState:
        # Return the successor state of the given state after taking the given action.
        print("get_successor_state is thinking...")
        x = action.position[1]
        y = action.position[0]

        playerModifier = 1
        if state.player1_turn:
            playerModifier = -1

        if y < len(state.board_status) and x < len(state.board_status):
            state.board_status[y][x] = (abs(state.board_status[y][x]) + 1) * playerModifier
        
        if action.action_type == "row":
            state.row_status[y][x] = 1
            if y >= 1:
                state.board_status[y - 1][x] = (abs(state.board_status[y - 1][x]) + 1) * playerModifier
        
        elif action.action_type == "col":
            state.col_status[y][x] = 1
            if x >= 1:
                state.board_status[y][x - 1] = (abs(state.board_status[y][x - 1]) + 1) * playerModifier
        

        return state

    def evaluate(self, state: GameState) -> int:
        # Return the evaluation value of the given state.
        # The evaluation value is the number of boxes filled by the current player.



        return np.sum(state.board_status == self.get_player_id(state))

    def get_player_id(self, state: GameState) -> int:
        # Return the player id of the given state.
        # The player id is 1 or 2.

        if(state.player1_turn):
            return -4
        else:
            return 4