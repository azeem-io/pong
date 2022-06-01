
from typing import Tuple


def map_value_to_range(value : int, current_range : Tuple, target_range : Tuple ):
    current_range_size = current_range[1] - current_range[0]
    target_range_size = target_range[1] - target_range[0]
    return (target_range_size/current_range_size)*(value - max(current_range[0],0))

