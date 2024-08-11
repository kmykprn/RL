import numpy as np
from commonUtils import get_possible_actions
from typing import Tuple, Dict, List

# 2次元リストの型ヒントを指定
EnvType = List[List[int]]


class GetNextState():

    def __init__(self, env: EnvType, row_size: int, col_size: int, seed: int) -> None:
        self.env = env
        self.row_size = row_size
        self.col_size = col_size
        np.random.seed(seed)


    def calculate_next_state(self, state: Tuple[int, int], action: str) -> Tuple[int, int]:
        """
        行動を実行した場合に遷移する状態（座標）を計算

        Args:
            state (Tuple[int, int]): 現在の座標
            action (str): 行動のキー

        Returns:
            next_state (Tuple[int, int]): 行動を実行した場合に遷移する状態
        """

        next_state = list(state)

        if action == 'up':
            next_state[0] -= 1
        elif action == 'down':
            next_state[0] += 1
        elif action == 'left':
            next_state[1] -= 1
        elif action == 'right':
            next_state[1] += 1

        # 返却する座標がenvのサイズを超えないようにする
        if (0 <= next_state[0] < self.row_size) and (0 <= next_state[1] < self.col_size):
            if self.env[next_state[0]][next_state[1]] != 9:
                return tuple(next_state)

        return state


    def calculcate_doAction_probabilities(self, ordered_action: str) -> Dict[str, float]:
        """
        ある行動命令に対し、各行動候補が実行されうる確率を計算

        Args:
            ordered_action (str): 行動のキー

        Returns:
            action_probabilities (Dict[str, float]): 行動のキーと、遷移確率のセット
        """

        # 指定された行動の反対方向を取得する。'up'なら'down'を返す。
        opposites = {
            'up': 'down',
            'down': 'up',
            'right': 'left',
            'left': 'right'
        }
        opposite_action = opposites.get(ordered_action)

        # 行動の候補を取得
        actions = get_possible_actions()
        actions_key_list = list(actions.keys())

        # 各行動の候補が実行されうる確率を計算
        action_probabilities = {}
        for a in actions_key_list:

            if a == ordered_action:
                prob = 0.8
            elif a == opposite_action:
                prob = 0
            else:
                prob = (1 - 0.8) / 2

            action_probabilities[a] = action_probabilities.get(a, 0) + prob

        # {'up': 0.8, 'down': 0, 'right': 0.1, 'left': 0.1}
        return action_probabilities


    def mainProcess(self, state: Tuple[int, int], action: str) -> Tuple[int, int]:
        """
        行動リスト内の各行動ごとに、「行動を実行した場合に遷移する状態（座標）」と、「実行される確率」を取得

        Args:
            state (tuple): 現在の座標
            action (str): 行動のキー
            env (EnvType): 環境

        Returns:
            next_state (tuple): 次の座標
        """

        # ある行動命令に対し、各行動候補が実行されうる確率を計算。例.{'up': 0.8, 'down': 0, 'right': 0.1, 'left': 0.1}
        action_probs = self.calculcate_doAction_probabilities(ordered_action=action)

        # 行動リスト内の各行動ごとに、「行動を実行した場合に遷移する状態（座標）」と、「実行される確率」を取得
        # next_states例: ['[0, 1]', '[1, 0]', '[2, 0]']。probs例: [0.8, 0.1, 0.1]
        transition_probs = {}
        for a, prob in action_probs.items():
            next_state_str = str(list(self.calculate_next_state(state=state, action=a)))
            transition_probs[next_state_str] = transition_probs.get(next_state_str, 0) + prob

        next_states = list(transition_probs.keys())
        probs = list(transition_probs.values())

        # 遷移確率を踏まえて、次の行動を選択
        next_state_str = np.random.choice(next_states, p=probs)

        # tupleに変換して返す
        return eval(next_state_str)