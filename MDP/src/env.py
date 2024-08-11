from typing import List, Tuple
import numpy as np

# 2次元リストの型ヒントを指定
EnvType = List[List[int]]


class Environment():

    def __init__(self) -> None:
        self.env: EnvType = [
            [0, 0, 0, 1],
            [0, 9, 0, -1],
            [0, 0, 0, 0]
        ]


    def get_env(self) -> EnvType:
        return self.env


    def get_env_dimensions(self) -> Tuple[int, int]:
        """
        環境の行数と列数を取得する

        Args:
            - env (EnvType): 2次元配列。例.
            - env: EnvType = [
                [0, 0, 0, 1],
                [0, 9, 0, -1],
                [0, 0, 0, 0]
            ]

        Returns:
            - row_size: int
            - col_size: int
        """

        env_array = np.array(self.env)

        # envの行数、列数を取得
        shape = env_array.shape
        row_size = shape[0]
        col_size = shape[1]

        return row_size, col_size