#!/usr/bin/env python3
"""Reproducible geometry checks for the provisional 20:1 gearbox baseline."""

from dataclasses import dataclass
from fractions import Fraction

PRESSURE_ANGLE_DEG = 20.0
HEX12_CIRCUMSCRIBED_DIAMETER_MM = 13.856
MODULE_MM = 1.5


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


def hex_radial_root_wall_mm(pinion: Gear) -> float:
    return (pinion.root_diameter_mm - HEX12_CIRCUMSCRIBED_DIAMETER_MM) / 2


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


if __name__ == "__main__":
    main()
