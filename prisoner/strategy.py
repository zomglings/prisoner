from typing import Callable

from .data import Action, GameState, Strategy


def always_cooperate(state: GameState, player_index: int) -> Action:
    return Action.COOPERATE


def always_defect(state: GameState, player_index: int) -> Action:
    return Action.DEFECT


def tit_for_tat(state: GameState, player_index: int) -> Action:
    if not state.history:
        return Action.COOPERATE
    opponent_index = 1 - player_index
    last_opponent_action = state.history[-1][opponent_index][2]
    return last_opponent_action


def vengeful(state: GameState, player_index: int) -> Action:
    if not state.history:
        return Action.COOPERATE
    opponent_index = 1 - player_index
    for round in state.history:
        if round[opponent_index][2] == Action.DEFECT:
            return Action.DEFECT
    return Action.COOPERATE


def opponent_majority(state: GameState, player_index: int) -> Action:
    opponent_index = 1 - player_index
    opponent_majority = sum(
        round[opponent_index][2] == Action.DEFECT for round in state.history
    ) >= int(len(state.history) / 2)
    return Action.DEFECT if opponent_majority else Action.COOPERATE


STRATEGIES: dict[Strategy, Callable[[GameState, int], Action]] = {
    Strategy.ALWAYS_COOPERATE: always_cooperate,
    Strategy.ALWAYS_DEFECT: always_defect,
    Strategy.TIT_FOR_TAT: tit_for_tat,
    Strategy.VENGEFUL: vengeful,
}
