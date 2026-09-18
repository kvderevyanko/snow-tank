# Requirements

## Scope

This project designs a compact RC tracked vehicle for deep, loose snow. The
drivetrain uses two independent 775-class brushed motors, one per track.

## Current drivetrain requirements

| ID | Requirement | Status |
| --- | --- | --- |
| DR-001 | The gearbox shall have two spur-gear reduction stages per track. | Geometric baseline |
| DR-002 | The geometric reduction shall be exactly 20:1. | Geometric baseline |
| DR-003 | Both geometric-baseline stages shall use module 1.5 mm and 20 degree pressure angle. | Geometric baseline |
| DR-004 | The motor pinion shall use the fixed HEX12 torque interface; M4 axial retention shall not transmit primary torque. | Interface baseline |
| DR-005 | The maximum outside diameter of a baseline gear shall be no more than 124.5 mm. | Geometric baseline |
| DR-006 | CAD for the motor pinion shall not be created before the HEX12 axial length is measured. | Open constraint |
| DR-007 | The baseline shall not be called strength-approved or final before motor, material, and load verification. | Open constraint |

## Out of scope for this stage

- CAD geometry, STL generation, and printed parts;
- shaft and bearing selection;
- final face widths;
- strength, wear, thermal, or life approval;
- motor speed, torque, and vehicle-speed estimates.

See [decisions.md](decisions.md), [measurements.md](measurements.md), and
[gearbox-study.md](gearbox-study.md).
