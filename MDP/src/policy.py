import random
from commonUtils import get_possible_actions


class Policy():
    def __init__(self, seed) -> None:
        random.seed(seed)


    def random_choice(self) -> str:
        """
        行動の候補から、ランダムに行動を選択する

        Returns:
            str: 選択された行動のキー (例. 'up')
        """
        actions_dict = get_possible_actions()
        actions_list = list(actions_dict.keys())
        action = random.choice(actions_list)
        return action