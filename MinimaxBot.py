from Bot import Bot
from GameAction import GameAction
from GameState import GameState
import numpy as np

class MinimaxBot(Bot):
    def get_action(self, state: GameState) -> GameAction:
        depth = len(np.argwhere(state.row_status == 0)) + len(np.argwhere(state.col_status == 0))
        return self.minimax(state, depth, -np.inf, np.inf, True)

    def minimax(self, state: GameState, depth: int, alpha: bool, beta: bool, maximizingPlayer: bool):
        if depth == 0 or self.is_terminal(state):
            return self.evaluate(state)
        
        if maximizingPlayer:
            maxValue = -np.inf
            for child in self.get_succ(GameState(state.board_status, state.row_status, state.col_status, state.player1_turn)):
                value = self.minimax(child, depth - 1, alpha, beta, False)
                maxValue = max(maxValue, value)
                alpha = max(alpha, maxValue)      
                if (beta <= alpha):
                    break
                print("max", maxValue)
            return maxValue
        else:
            minValue = np.inf
            for child in self.get_succ(GameState(state.board_status, state.row_status, state.col_status, not state.player1_turn)):
                value = self.minimax(child, depth - 1, alpha, beta, True)
                minValue = min(minValue, value)
                beta = min(beta, value)  
                if (beta <= alpha):
                    break
            return minValue

    def is_terminal(self, state: GameState) -> bool:
        # Check if the given state is terminal.
        return (state.row_status == 1).all() and (state.col_status == 1).all()

    def evaluate(self, state: GameState) -> int:
        # Return the evaluation of the given state.
        player1_score = len(np.argwhere(state.board_status == -4))
        player2_score = len(np.argwhere(state.board_status == 4))
        if(state.player1_turn):
            if(player1_score > player2_score):
                return 1
            else:
                return -1
        else:
            if(player1_score < player2_score):
                return 1
            else:
                return -1

    def get_successors(self, state: GameState) -> list[GameAction]:
        # Return a list of all successor states of the given state.
        successors = []
        
        [y,x] = state.row_status.shape

        for i in range(y):
            for j in range(x):
                if state.row_status[i][j] == 0:
                    successors.append(GameAction("row", (i, j)))

        [y,x] = state.col_status.shape
        for i in range(y):
            for j in range(x):
                if state.col_status[i][j] == 0:
                    successors.append(GameAction("col", (i, j)))

        return successors

    def get_successor_state(self, state: GameState, action: GameAction) -> GameState:
        # Return the successor state of the given state after taking the given action.

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

    def get_succ(self, state: GameState) -> GameState:
        succ = []

        for action in self.get_successors(state):
            succ.append(self.get_successor_state(GameState(
                state.board_status.copy(),
                state.row_status.copy(),
                state.col_status.copy(),
                state.player1_turn), action))
        
        return succ
