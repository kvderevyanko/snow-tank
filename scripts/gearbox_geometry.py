#!/usr/bin/env python3
"""Reproducible geometry checks for the provisional 20:1 gearbox baseline."""

from dataclasses import dataclass
from fractions import Fraction
from math import cos, pi, radians

PRESSURE_ANGLE_DEG = 20.0
HEX_ACROSS_FLATS_MM = 12.0
MODULE_MM = 1.5
M3_CLEARANCE_DIAMETER_MM = 3.2

# Dimensions below are owner-provided nominal data, not supplier-verified data.
BEARING_688 = (8.0, 16.0, 5.0)
BEARING_22_TBD_X_6 = (None, 22.0, 6.0)
BEARING_6001 = (12.0, 28.0, 8.0)


@dataclass(frozen=True)
class Gear:
    teeth: int
    module_mm: float = MODULE_MM

    @property
    def pitch_diameter_mm(self) -> float:
        return self.module_mm * self.teeth

    @property
    def outside_diameter_mm(self) -> float:
        return self.module_mm * (self.teeth + 2)

    @property
    def root_diameter_mm(self) -> float:
        return self.module_mm * (self.teeth - 2.5)


@dataclass(frozen=True)
class Stage:
    pinion: Gear
    gear: Gear

    @property
    def ratio(self) -> Fraction:
        return Fraction(self.gear.teeth, self.pinion.teeth)

    @property
    def center_distance_mm(self) -> float:
        if self.pinion.module_mm != self.gear.module_mm:
            raise ValueError("A meshing gear pair must use one module")
        return (self.pinion.pitch_diameter_mm + self.gear.pitch_diameter_mm) / 2


STAGE_1 = Stage(Gear(18), Gear(80))
STAGE_2 = Stage(Gear(18), Gear(81))


def total_ratio() -> Fraction:
    return STAGE_1.ratio * STAGE_2.ratio


def hex_circumscribed_diameter_mm() -> float:
    """Return a regular HEX12 corner-to-corner diameter from its across-flats size."""
    return HEX_ACROSS_FLATS_MM / cos(radians(30.0))


def hex_radial_root_wall_mm(pinion: Gear) -> float:
    return (pinion.root_diameter_mm - hex_circumscribed_diameter_mm()) / 2


def annular_radial_wall_mm(
    outer_diameter_mm: float, bore_diameter_mm: float = M3_CLEARANCE_DIAMETER_MM
) -> float:
    """Nominal radial nylon wall around the axial clearance bore."""
    return (outer_diameter_mm - bore_diameter_mm) / 2


def annular_second_moment_mm4(
    outer_diameter_mm: float, bore_diameter_mm: float = M3_CLEARANCE_DIAMETER_MM
) -> float:
    """Area second moment I of a circular annulus about a centroidal bend axis."""
    return pi / 64 * (outer_diameter_mm**4 - bore_diameter_mm**4)


def annular_polar_moment_mm4(
    outer_diameter_mm: float, bore_diameter_mm: float = M3_CLEARANCE_DIAMETER_MM
) -> float:
    """Polar second moment J of a circular annulus; geometric torsion comparison only."""
    return pi / 32 * (outer_diameter_mm**4 - bore_diameter_mm**4)


def annular_section_modulus_mm3(
    outer_diameter_mm: float, bore_diameter_mm: float = M3_CLEARANCE_DIAMETER_MM
) -> float:
    return annular_second_moment_mm4(outer_diameter_mm, bore_diameter_mm) / (
        outer_diameter_mm / 2
    )


def main() -> None:
    stages = (STAGE_1, STAGE_2)
    for index, stage in enumerate(stages, start=1):
        print(f"stage {index}: {stage.pinion.teeth}T -> {stage.gear.teeth}T")
        print(f"  ratio: {stage.ratio} = {float(stage.ratio):.9f}")
        print(
            "  pitch diameters: "
            f"{stage.pinion.pitch_diameter_mm:.3f} / "
            f"{stage.gear.pitch_diameter_mm:.3f} mm"
        )
        print(
            "  outside diameters: "
            f"{stage.pinion.outside_diameter_mm:.3f} / "
            f"{stage.gear.outside_diameter_mm:.3f} mm"
        )
        print(
            "  root diameters: "
            f"{stage.pinion.root_diameter_mm:.3f} / "
            f"{stage.gear.root_diameter_mm:.3f} mm"
        )
        print(f"  center distance: {stage.center_distance_mm:.3f} mm")
    print(f"total ratio: {total_ratio()} = {float(total_ratio()):.9f}")
    print(
        "motor-pinion HEX12 radial root wall: "
        f"{hex_radial_root_wall_mm(STAGE_1.pinion):.3f} mm"
    )
    print(
        "linear motor-axis to output-axis distance: "
        f"{sum(stage.center_distance_mm for stage in stages):.3f} mm"
    )
    print(f"M3 clearance bore: {M3_CLEARANCE_DIAMETER_MM:.3f} mm")
    reference_i = annular_second_moment_mm4(8.0)
    for diameter in (8.0, 10.0, 12.0):
        inertia = annular_second_moment_mm4(diameter)
        print(
            f"journal {diameter:.0f} mm: wall "
            f"{annular_radial_wall_mm(diameter):.3f} mm; "
            f"I {inertia:.3f} mm^4 ({inertia / reference_i:.3f}x 8 mm); "
            f"J {annular_polar_moment_mm4(diameter):.3f} mm^4; "
            f"Z {annular_section_modulus_mm3(diameter):.3f} mm^3"
        )


if __name__ == "__main__":
    main()
