from typing import Tuple, List


# 2次元リストの型ヒントを指定
EnvType = List[List[int]]


def calculcate_reward(state: Tuple[int, int], env: EnvType) -> Tuple[float, bool]:
    """
    状態に基づいて報酬を計算する。

    Args:
        state (StateType): 報酬を計算したい座標
        env (EnvType): 環境を表す2次元リスト

    Returns:
        (reward, isFinished) (tuple): 報酬と終了状態のタプル
    """
    default_reward = -0.04
    state_row, state_col = state
    env_value = env[state_row][state_col]

    if env_value == 1:
        reward = 1
    elif env_value == -1:
        reward = -1
    else:
        reward = default_reward

    return reward