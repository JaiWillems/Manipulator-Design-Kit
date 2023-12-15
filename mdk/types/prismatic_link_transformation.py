import numpy as np

from mdk.types.link_transformation import LinkTransformation


class PrismaticLinkTransformation(LinkTransformation):

    def __init__(
            self,
            link_length: float,
            twist_angle: float,
            joint_angle: float
    ) -> None:

        self._link_length = link_length
        self._twist_angle = twist_angle
        self._joint_angle = joint_angle

    def evaluate(self, link_offset: float) -> np.ndarray:
        return LinkTransformation._transformation(
            self._link_length,
            self._twist_angle,
            link_offset,
            self._joint_angle
        )
