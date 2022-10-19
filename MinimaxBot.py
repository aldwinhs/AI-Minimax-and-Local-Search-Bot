from Bot import Bot
from GameAction import GameAction
from GameState import GameState
from Objective import Objective
import numpy as np
import time


class MinimaxBot(Bot):
    execTimeStart = 0

    def get_action(self, state: GameState) -> GameAction:
        depth = len(np.argwhere(state.row_status == 0)) + \
            len(np.argwhere(state.col_status == 0))
        self.execTimeStart = time.time()

        if (depth == 1):
            BestAction = Objective.get_action_successors(state)[0]
        else:
            BestAction = None
            maxValue = -np.inf
            for action in Objective.get_action_successors(state):
                value = self.minimax(Objective.get_successor_state(GameState(
                    state.board_status.copy(),
                    state.row_status.copy(),
                    state.col_status.copy(),
                    state.player1_turn), action), depth-1, -np.inf, np.inf, False, state.player1_turn)
                if value > maxValue:
                    maxValue = value
                    BestAction = action

        print("Thinking time: ", time.time()-self.execTimeStart)
        return GameAction(BestAction.action_type, (BestAction.position[1], BestAction.position[0]))

    def minimax(self, state: GameState, depth: int, alpha, beta, maximizingPlayer: bool, botTurn: bool):
        if depth == 0 or self.is_terminal(state) or (time.time()-self.execTimeStart > 5):
            return self.evaluate(state, botTurn)

        if maximizingPlayer:
            maxValue = -np.inf
            for child in self.get_successors(GameState(state.board_status, state.row_status, state.col_status, state.player1_turn)):
                value = self.minimax(
                    child, depth - 1, alpha, beta, False, botTurn)
                maxValue = max(maxValue, value)
                alpha = max(alpha, maxValue)
                if (beta <= alpha):
                    break
            return maxValue
        else:
            minValue = np.inf
            for child in self.get_successors(GameState(state.board_status, state.row_status, state.col_status, not state.player1_turn)):
                value = self.minimax(
                    child, depth - 1, alpha, beta, True, botTurn)
                minValue = min(minValue, value)
                beta = min(beta, value)
                if (beta <= alpha):
                    break
            return minValue

    def is_terminal(self, state: GameState) -> bool:
        # Check if the given state is terminal.
        return (state.row_status == 1).all() and (state.col_status == 1).all()

    def evaluate(self, state: GameState, botTurn) -> int:
        # Return the evaluation of the given state.
        player1_score = len(np.argwhere(state.board_status == -4))
        player2_score = len(np.argwhere(state.board_status == 4))
        if (botTurn):
            return player1_score - player2_score
        else:
            return player2_score - player1_score

    def get_successors(self, state: GameState) -> GameState:
        succ = []

        for action in Objective.get_action_successors(state):
            succ.append(Objective.get_successor_state(GameState(
                state.board_status.copy(),
                state.row_status.copy(),
                state.col_status.copy(),
                state.player1_turn), action))

        return succ
