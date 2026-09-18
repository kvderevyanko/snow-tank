# Requirements

## Scope

This project designs a compact RC tracked vehicle for deep, loose snow. The
drivetrain uses two independent 775-class brushed motors, one per track.

## Current drivetrain requirements

| ID | Requirement | Status |
| --- | --- | --- |
| DR-001 | The gearbox shall have two spur-gear reduction stages per track. | Geometric baseline |
| DR-002 | Target gearbox reduction is approximately 20:1. | Product target |
| DR-003 | Packaging target for the largest gear outside diameter is approximately <=125 mm. | Product target |
| DR-004 | The motor pinion shall use the fixed HEX12 torque interface; M4 axial retention shall not transmit primary torque. | Interface baseline |
| DR-005 | CAD for the motor pinion shall not be created before the HEX12 axial length is measured. | Open constraint |
| DR-006 | The baseline shall not be called strength-approved or final before motor, material, and load verification. | Open constraint |

## Current D-001 geometric baseline

D-001 is a provisional design decision, not an immutable product requirement:

- exactly 20:1 total reduction;
- module 1.5 mm and 20 degree pressure angle on both stages;
- 18T -> 80T on stage 1 and 18T -> 81T on stage 2;
- maximum outside diameter 124.5 mm.

## Out of scope for this stage

- CAD geometry, STL generation, and printed parts;
- shaft and bearing selection;
- final face widths;
- strength, wear, thermal, or life approval;
- motor speed, torque, and vehicle-speed estimates.

See [decisions.md](decisions.md), [measurements.md](measurements.md), and
[gearbox-study.md](gearbox-study.md).
