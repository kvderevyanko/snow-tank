"""Tests for the provisional gearbox geometric baseline."""

from fractions import Fraction
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from gearbox_geometry import (  # noqa: E402
    HEX12_CIRCUMSCRIBED_DIAMETER_MM,
    PRESSURE_ANGLE_DEG,
    STAGE_1,
    STAGE_2,
    hex_radial_root_wall_mm,
    total_ratio,
)


class GearboxBaselineTests(unittest.TestCase):
    def test_ratio_is_exactly_twenty_to_one(self) -> None:
        self.assertEqual(STAGE_1.ratio, Fraction(40, 9))
        self.assertEqual(STAGE_2.ratio, Fraction(9, 2))
        self.assertEqual(total_ratio(), Fraction(20, 1))

    def test_stage_one_geometry(self) -> None:
        self.assertEqual(STAGE_1.pinion.pitch_diameter_mm, 27.0)
        self.assertEqual(STAGE_1.gear.pitch_diameter_mm, 120.0)
        self.assertEqual(STAGE_1.pinion.outside_diameter_mm, 30.0)
        self.assertEqual(STAGE_1.gear.outside_diameter_mm, 123.0)
        self.assertEqual(STAGE_1.pinion.root_diameter_mm, 23.25)
        self.assertEqual(STAGE_1.gear.root_diameter_mm, 116.25)
        self.assertEqual(STAGE_1.center_distance_mm, 73.5)

    def test_stage_two_geometry(self) -> None:
        self.assertEqual(STAGE_2.pinion.pitch_diameter_mm, 27.0)
        self.assertEqual(STAGE_2.gear.pitch_diameter_mm, 121.5)
        self.assertEqual(STAGE_2.pinion.outside_diameter_mm, 30.0)
        self.assertEqual(STAGE_2.gear.outside_diameter_mm, 124.5)
        self.assertEqual(STAGE_2.pinion.root_diameter_mm, 23.25)
        self.assertEqual(STAGE_2.gear.root_diameter_mm, 117.75)
        self.assertEqual(STAGE_2.center_distance_mm, 74.25)

    def test_layout_and_hex_wall(self) -> None:
        self.assertEqual(PRESSURE_ANGLE_DEG, 20.0)
        self.assertEqual(HEX12_CIRCUMSCRIBED_DIAMETER_MM, 13.856)
        self.assertEqual(
            STAGE_1.center_distance_mm + STAGE_2.center_distance_mm, 147.75
        )
        self.assertAlmostEqual(hex_radial_root_wall_mm(STAGE_1.pinion), 4.697)
        self.assertGreaterEqual(hex_radial_root_wall_mm(STAGE_1.pinion), 3.5)


if __name__ == "__main__":
    unittest.main()
