from typing import Dict, List


# 2次元リストの型ヒントを指定
EnvType = List[List[int]]


def get_possible_actions() -> Dict[str, int]:
    """
    行動の候補を取得する
    """
    return {
        'up': 1,
        'down': -1,
        'left': 2,
        'right': -2
    }