import numpy as np

from mdk.types.link import Link


class RevoluteLink(Link):

    def __init__(
            self,
            link_length: float,
            twist_angle: float,
            link_offset: float
    ) -> None:

        self._link_length = link_length
        self._twist_angle = twist_angle
        self._link_offset = link_offset

    def transformation(self, joint_angle: float) -> np.ndarray:
        return Link._transformation(
            self._link_length,
            self._twist_angle,
            self._link_offset,
            joint_angle
        )
