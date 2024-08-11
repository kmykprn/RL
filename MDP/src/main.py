from env import Environment
from policy import Policy
from rl import RL


if __name__ == '__main__':

    # 環境を構築するためのインスタンスを生成
    e = Environment()

    # 行動選択のポリシーを設定するためのインスタンスを生成
    p = Policy()

    # 何エピソード学習するか？を設定
    episode_num = 10

    # ランダムのシード値を設定
    seed = 0

    # 強化学習の実施（出力はtotal_reward)
    total_reward_list_by_episode = RL(e, p, episode_num, seed)

    # 出力の表示
    for i, total_reward in enumerate(total_reward_list_by_episode):
        print(f'Episode {i}: Agent gets {total_reward} reward')

