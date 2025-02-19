from typing import List, Optional, Tuple

class Turn:
    BLACK: "Turn"
    WHITE: "Turn"

    def __eq__(self, other: object) -> bool: ...
    def __str__(self) -> str: ...

class Color:
    EMPTY: "Color"
    BLACK: "Color"
    WHITE: "Color"

    def __eq__(self, other: object) -> bool: ...
    def __str__(self) -> str: ...

class Board:
    def __init__(self) -> None: ...
    def get_board(self) -> Tuple[int, int, Turn]: ...
    def get_turn(self) -> Turn: ...
    def set_board(self, player_board: int, opponent_board: int, turn: Turn) -> None: ...
    def set_board_str(self, line: str, turn: Turn) -> None: ...
    def get_board_line(self) -> str: ...
    def get_board_vec_black(self) -> List[Color]: ...
    def get_board_vec_turn(self) -> List[Color]: ...
    def get_board_matrix(self) -> List[List[List[int]]]: ...
    def player_piece_num(self) -> int: ...
    def opponent_piece_num(self) -> int: ...
    def black_piece_num(self) -> int: ...
    def white_piece_num(self) -> int: ...
    def piece_sum(self) -> int: ...
    def diff_piece_num(self) -> int: ...
    def get_legal_moves(self) -> int: ...
    def get_legal_moves_vec(self) -> List[int]: ...
    def get_legal_moves_tf(self) -> List[bool]: ...
    def is_legal_move(self, pos: int) -> bool: ...
    def get_child_boards(self) -> List["Board"]: ...
    def do_move(self, pos: int) -> None: ...
    def do_pass(self) -> None: ...
    def is_pass(self) -> bool: ...
    def is_game_over(self) -> bool: ...
    def is_win(self) -> bool: ...
    def is_lose(self) -> bool: ...
    def is_draw(self) -> bool: ...
    def is_black_win(self) -> bool: ...
    def is_white_win(self) -> bool: ...
    def get_winner(self) -> Optional[Turn]: ...
    def get_random_move(self) -> int: ...
    def __str__(self) -> str: ...
    def clone(self) -> "Board": ...

class Arena:
    def __init__(
        self, command1: List[str], command2: List[str], show_progress: bool = True
    ) -> None: ...
    def play_n(self, n: int) -> None: ...
    def get_stats(self) -> Tuple[int, int, int]: ...
    def get_pieces(self) -> Tuple[int, int]: ...

class NetworkArenaServer:
    def __init__(self, game_per_iter: int, show_progress: bool = True) -> None: ...
    def start(self, address: str, port: int) -> None: ...

class NetworkArenaClient:
    def __init__(self, command: List[str]) -> None: ...
    def connect(self, address: str, port: int) -> None: ...
    def get_stats(self) -> Tuple[int, int, int]: ...
    def get_pieces(self) -> Tuple[int, int]: ...

class Evaluator:
    def __init__(self) -> None: ...
    def evaluate(self, board: Board) -> int: ...
    def set_py_evaluator(self, evaluator: "Evaluator") -> None: ...

class PieceEvaluator(Evaluator):
    def __init__(self) -> None: ...
    def evaluate(self, board: Board) -> int: ...

class LegalNumEvaluator(Evaluator):
    def __init__(self) -> None: ...
    def evaluate(self, board: Board) -> int: ...

class MatrixEvaluator(Evaluator):
    def __init__(self, matrix: List[List[int]]) -> None: ...
    def evaluate(self, board: Board) -> int: ...

class AlphaBetaSearch:
    def __init__(self, evaluator: Evaluator, depth: int, win_score: int) -> None: ...
    def get_move(self, board: Board) -> int: ...
    def get_move_with_timeout(self, board: Board, timeout_ms: int) -> int: ...
    def get_search_score(self, board: Board) -> float: ...

class WinrateEvaluator:
    def __init__(self) -> None: ...
    def evaluate(self, board: Board) -> float: ...
    def set_py_evaluator(self, evaluator: "WinrateEvaluator") -> None: ...

class ThunderSearch:
    def __init__(
        self, evaluator: WinrateEvaluator, n_playout: int, epsilon: float
    ) -> None: ...
    def get_move(self, board: Board) -> int: ...
    def get_move_with_timeout(self, board: Board, timeout_ms: int) -> int: ...
    def get_search_score(self, board: Board) -> float: ...

class MctsSearch:
    """Monte Carlo Tree Search Search"""

    def __init__(self, n_playout: int, c: float, expand_threshold: int) -> None: ...
    """Initialize MctsSearch
    Args:
        n_playout: Number of playouts
        c: Exploration constant. c=1.0 is a good default value
        expand_threshold: Threshold for expanding the tree. expand_threshold=10 is a good default value
    """
    def get_move(self, board: Board) -> int: ...
    def get_move_with_timeout(self, board: Board, timeout_ms: int) -> int: ...
    def get_search_score(self, board: Board) -> float: ...
