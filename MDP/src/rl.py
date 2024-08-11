from typing import List
from reward import calculcate_reward
from getNextState import GetNextState


def RL(e, p, episode_num, seed=0) -> List[float]:

    # 環境を取得
    env = e.get_env()

    # envのサイズを取得
    row_size, col_size = e.get_env_dimensions()

    # 次の状態を計算するためのインスタンスを生成
    get_next_state = GetNextState(env=env, row_size=row_size, col_size=col_size, seed=seed)

    # 強化学習のメインプロセス
    total_reward_list_by_episode = []
    for i in range(episode_num):

        # パラメータの初期化
        state = (row_size - 1, 0)
        reward = 0
        total_reward = 0

        while True:

            if reward == 1 or reward == -1:
                break

            # 行動の候補の中から、ランダムに行動を選択。例. policyA() -> 'left'
            action = p.random_choice()

            # 行動に基づき、次の状態を計算。mainProcess(state: (0, 0), action: 'right') -> (0, 1):
            next_state = get_next_state.mainProcess(state=state, action=action)

            # 次の状態と環境に基づき、報酬を取得。calculcate_reward(state: (0, 1), env: env) -> (-0.04, False):
            reward = calculcate_reward(state=next_state, env=env)
            total_reward += reward

            # 現在の状態を更新
            state = next_state

        total_reward_list_by_episode.append(total_reward)

    return total_reward_list_by_episode