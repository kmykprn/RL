from rl import RL
from env import Environment
from policy import Policy


# Episode5までのトータルリワード値が、正解と一致するか. ただしseed=0.
def test_total_reward_correctness_to_episode_5():
    # 環境を構築するためのインスタンスを生成
    e = Environment()

    # シード値を設定
    seed = 0

    # 行動選択のポリシーを設定するためのインスタンスを生成
    p = Policy(seed=seed)

    # 何エピソード学習するか？を設定
    episode_num = 10

    # 強化学習の実施（出力はtotal_reward)
    total_reward_list_by_episode = RL(e, p, episode_num, seed)

    assert total_reward_list_by_episode[0] == -1.16
    assert total_reward_list_by_episode[1] == -1.7200000000000015
    assert total_reward_list_by_episode[2] == -1.4000000000000012
    assert total_reward_list_by_episode[3] == -2.960000000000001
    assert total_reward_list_by_episode[4] == -1.3599999999999999