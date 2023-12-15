import numpy as np

from mdk.types.link import Link


class PrismaticLink(Link):

    def __init__(
            self,
            link_length: float,
            twist_angle: float,
            joint_angle: float
    ) -> None:

        self._link_length = link_length
        self._twist_angle = twist_angle
        self._joint_angle = joint_angle

    def transformation(self, link_offset: float) -> np.ndarray:
        return Link._transformation(
            self._link_length,
            self._twist_angle,
            link_offset,
            self._joint_angle
        )
