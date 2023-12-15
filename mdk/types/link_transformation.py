import abc

import numpy as np


class LinkTransformation(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def evaluate(self, joint_variable: float) -> np.ndarray:
        raise NotImplementedError

    @staticmethod
    def _transformation(
            link_length: float,
            twist_angle: float,
            link_offset: float,
            joint_angle: float
    ) -> np.ndarray:
        return np.array([
            [np.cos(joint_angle), -np.sin(joint_angle) * np.cos(twist_angle),
             np.sin(joint_angle) * np.sin(twist_angle),
             link_length * np.cos(joint_angle)],
            [np.sin(joint_angle), np.cos(joint_angle) * np.cos(twist_angle),
             -np.cos(joint_angle) * np.sin(twist_angle),
             link_length * np.sin(joint_angle)],
            [0, np.sin(twist_angle), np.cos(twist_angle), link_offset],
            [0, 0, 0, 1]
        ])
