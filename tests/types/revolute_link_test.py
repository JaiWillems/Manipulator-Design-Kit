from unittest import TestCase

import numpy as np

from mdk.types.link import Link
from mdk.types.revolute_link import RevoluteLink


class RevoluteLinkTest(TestCase):

    def test_transformation_returns_successful_result(self) -> None:

        link_length = 1
        twist_angle = 1
        link_offset = 1
        joint_angle = 1

        expected = Link._transformation(
            link_length,
            twist_angle,
            link_offset,
            joint_angle
        )
        actual = RevoluteLink(
            link_length,
            twist_angle,
            link_offset
        ).transformation(joint_angle)

        self.assertTrue(np.array_equal(expected, actual))
