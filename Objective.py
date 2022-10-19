from GameState import GameState
from GameAction import GameAction
import random


class Objective():
    def get_action_successors(state: GameState) -> list[GameAction]:
        # Return a list of all successor states of the given state.
        successors = []

        [y, x] = state.row_status.shape

        for i in range(y):
            for j in range(x):
                if state.row_status[i][j] == 0:
                    successors.append(GameAction("row", (i, j)))

        [y, x] = state.col_status.shape
        for i in range(y):
            for j in range(x):
                if state.col_status[i][j] == 0:
                    successors.append(GameAction("col", (i, j)))

        random.shuffle(successors)
        return successors

    def get_successor_state(state: GameState, action: GameAction) -> GameState:
        # Return the successor state of the given state after taking the given action.

        x = action.position[1]
        y = action.position[0]

        playerModifier = 1
        if state.player1_turn:
            playerModifier = -1

        if y < len(state.board_status) and x < len(state.board_status):
            state.board_status[y][x] = (
                abs(state.board_status[y][x]) + 1) * playerModifier

        if action.action_type == "row":
            state.row_status[y][x] = 1
            if y >= 1:
                state.board_status[y - 1][x] = (
                    abs(state.board_status[y - 1][x]) + 1) * playerModifier

        elif action.action_type == "col":
            state.col_status[y][x] = 1
            if x >= 1:
                state.board_status[y][x - 1] = (
                    abs(state.board_status[y][x - 1]) + 1) * playerModifier

        return state
