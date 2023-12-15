import numpy as np

from mdk.types.link_transformation import LinkTransformation


class RevoluteLinkTransformation(LinkTransformation):

    def __init__(
            self,
            link_length: float,
            twist_angle: float,
            link_offset: float
    ) -> None:

        self._link_length = link_length
        self._twist_angle = twist_angle
        self._link_offset = link_offset

    def evaluate(self, joint_angle: float) -> np.ndarray:
        return LinkTransformation._transformation(
            self._link_length,
            self._twist_angle,
            self._link_offset,
            joint_angle
        )
