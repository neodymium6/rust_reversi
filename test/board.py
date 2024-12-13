from rust_reversi import Board, Turn, Color  # type: ignore


def test_init():
    board = Board()
    player_board, opponent_board, turn = board.get_board()
    assert player_board == 0x0000000810000000
    assert opponent_board == 0x0000001008000000
    assert turn == Turn.Black


def test_set_board():
    board = Board()
    player_board_t = 0x0000000000000000
    opponent_board_t = 0x0000000000000000
    turn_t = Turn.White
    board.set_board(player_board_t, opponent_board_t, turn_t)
    player_board, opponent_board, turn = board.get_board()
    assert player_board == player_board_t
    assert opponent_board == opponent_board_t
    assert turn == turn_t


def test_set_board_str():
    board = Board()
    board_str_t = "{}{}{}{}{}{}{}{}".format(
        "X" * 8,
        "-" * 8,
        "-" * 8,
        "-" * 8,
        "-" * 8,
        "-" * 8,
        "-" * 8,
        "O" * 8,
    )
    turn_t = Turn.Black
    board.set_board_str(board_str_t, turn_t)

    player_board, opponent_board, turn = board.get_board()
    assert player_board == 0xFF00000000000000
    assert opponent_board == 0x00000000000000FF
    assert turn == turn_t


def test_get_board_vec():
    board = Board()
    board_vec_t = [Color.Empty] * 64
    board_vec_t[27] = Color.White
    board_vec_t[28] = Color.Black
    board_vec_t[35] = Color.Black
    board_vec_t[36] = Color.White

    board_vec = board.get_board_vec()
    assert board_vec == board_vec_t


def test_get_board_matrix():
    board = Board()
    player_t = [[0] * 8 for _ in range(8)]
    player_t[4][3] = 1
    player_t[3][4] = 1
    opponent_t = [[0] * 8 for _ in range(8)]
    opponent_t[3][3] = 1
    opponent_t[4][4] = 1
    empty_t = [[1] * 8 for _ in range(8)]
    empty_t[3][3] = 0
    empty_t[3][4] = 0
    empty_t[4][3] = 0
    empty_t[4][4] = 0
    board_matrix_t = [player_t, opponent_t, empty_t]

    board_matrix = board.get_board_matrix()
    assert board_matrix == board_matrix_t


def test_piece_num():
    board = Board()
    board.set_board(0xF0000000000000FF, 0x0000000FF0000000, Turn.Black)
    player_num_t = 12
    opponent_num_t = 8
    assert board.player_piece_num() == player_num_t
    assert board.opponent_piece_num() == opponent_num_t
    assert board.black_piece_num() == player_num_t
    assert board.white_piece_num() == opponent_num_t
    assert board.piece_sum() == player_num_t + opponent_num_t
    assert board.diff_piece_num() == player_num_t - opponent_num_t


def test_get_legal_moves():
    board = Board()
    board_str_t = "{}{}{}{}{}{}{}{}".format(
        "--------",
        "--------",
        "--OOO---",
        "---OXX--",
        "--OOXX--",
        "--OX----",
        "--------",
        "--------",
    )
    turn_t = Turn.White
    board.set_board_str(board_str_t, turn_t)
    legal_moves_t = [21, 30, 38, 44, 45, 46, 51, 52]
    assert board.get_legal_moves_vec() == legal_moves_t
    board.set_board_str(board_str_t, Turn.Black)
    legal_moves_t = [9, 10, 11, 12, 25, 26, 33, 41, 49]
    assert board.get_legal_moves_vec() == legal_moves_t
