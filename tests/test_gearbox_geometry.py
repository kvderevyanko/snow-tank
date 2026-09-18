"""Tests for the provisional gearbox geometric baseline."""

from fractions import Fraction
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from gearbox_geometry import (  # noqa: E402
    BEARING_22_TBD_X_6,
    BEARING_6001,
    BEARING_688,
    HEX_ACROSS_FLATS_MM,
    M3_CLEARANCE_DIAMETER_MM,
    PRESSURE_ANGLE_DEG,
    STAGE_1,
    STAGE_2,
    annular_polar_moment_mm4,
    annular_radial_wall_mm,
    annular_second_moment_mm4,
    annular_section_modulus_mm3,
    hex_circumscribed_diameter_mm,
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
        self.assertEqual(HEX_ACROSS_FLATS_MM, 12.0)
        self.assertAlmostEqual(hex_circumscribed_diameter_mm(), 13.8564064606)
        self.assertEqual(
            STAGE_1.center_distance_mm + STAGE_2.center_distance_mm, 147.75
        )
        self.assertAlmostEqual(
            hex_radial_root_wall_mm(STAGE_1.pinion), 4.6967967697
        )
        self.assertGreaterEqual(hex_radial_root_wall_mm(STAGE_1.pinion), 3.5)

    def test_owner_reported_bearing_dimensions_remain_classified(self) -> None:
        self.assertEqual(BEARING_688, (8.0, 16.0, 5.0))
        self.assertEqual(BEARING_6001, (12.0, 28.0, 8.0))
        self.assertEqual(BEARING_22_TBD_X_6, (None, 22.0, 6.0))

    def test_m3_bored_journal_sections(self) -> None:
        self.assertEqual(M3_CLEARANCE_DIAMETER_MM, 3.2)
        self.assertAlmostEqual(annular_radial_wall_mm(8.0), 2.4)
        self.assertAlmostEqual(annular_radial_wall_mm(10.0), 3.4)
        self.assertAlmostEqual(annular_radial_wall_mm(12.0), 4.4)
        self.assertAlmostEqual(annular_second_moment_mm4(8.0), 195.9147444261)
        self.assertAlmostEqual(annular_second_moment_mm4(10.0), 485.7266667198)
        self.assertAlmostEqual(annular_polar_moment_mm4(10.0), 971.4533334395)
        self.assertAlmostEqual(annular_section_modulus_mm3(12.0), 168.7881390599)
        self.assertAlmostEqual(
            annular_second_moment_mm4(10.0) / annular_second_moment_mm4(8.0),
            2.4792757081,
        )


if __name__ == "__main__":
    unittest.main()
