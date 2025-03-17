from dataclasses import dataclass
from enum import Enum


class Action(Enum):
    COOPERATE = 0
    DEFECT = 1


class Strategy(Enum):
    ALWAYS_COOPERATE = "always_cooperate"
    ALWAYS_DEFECT = "always_defect"
    TIT_FOR_TAT = "tit_for_tat"
    VENGEFUL = "vengeful"
    OPPONENT_MAJORITY = "opponent_majority"


class ScoreMethod(Enum):
    STANDARD = "standard"
    HP = "hp"


@dataclass
class GameState:
    # Payoffs is a dictionary of the form:
    # {
    #     (Action.COOPERATE, Action.COOPERATE): <integer payoff to player in index 0 for this outcome>,
    #     (Action.COOPERATE, Action.DEFECT): <integer payoff to player in index 0 for this outcome>,
    #     (Action.DEFECT, Action.COOPERATE): <integer payoff to player in index 0 for this outcome>,
    #     (Action.DEFECT, Action.DEFECT): <integer payoff to player in index 0 for this outcome>,
    # }
    payoffs: dict[tuple[Action, Action], int]

    score_method: ScoreMethod
    # If True, weight discount is applied to past payoffs. If False, weight discount is applied to future payoffs.
    shadow_of_past: bool
    # Set to 0 to only consider:
    # - most recent round score (if shadow_of_past is True)
    # - first round score (if shadow_of_past is False)
    score_future_weight: float

    player_0_score: float
    player_1_score: float

    player_0_strategy: Strategy
    player_1_strategy: Strategy
    player_0_hp: int
    player_1_hp: int
    round: int
    game_over: bool

    # A list of tuples of the form:
    # (
    #     (player_0_hp_start, player_0_score_start, player_0_action, player_0_hp_end, player_0_score_end),
    #     (player_1_hp_start, player_1_score_start, player_1_action, player_1_hp_end, player_1_score_end)
    # )
    history: list[tuple[tuple[int, Action, int], tuple[int, Action, int]]]
