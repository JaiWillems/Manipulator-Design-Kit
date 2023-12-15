from unittest import TestCase

import numpy as np

from mdk.types.link_transformation import LinkTransformation
from mdk.types.revolute_link_transformation import RevoluteLinkTransformation


class RevoluteLinkTransformationTest(TestCase):

    def test_evaluate_returns_successful_result(self) -> None:

        link_length = 1
        twist_angle = 1
        link_offset = 1
        joint_angle = 1

        expected = LinkTransformation._transformation(
            link_length,
            twist_angle,
            link_offset,
            joint_angle
        )
        actual = RevoluteLinkTransformation(
            link_length,
            twist_angle,
            link_offset
        ).evaluate(joint_angle)

        self.assertTrue(np.array_equal(expected, actual))
