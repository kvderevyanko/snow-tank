# Engineering decisions

## D-001 — 20:1 two-stage gearbox geometric baseline

**Status: provisional geometric baseline.** This is not a validated or final
drivetrain design and is not strength-approved.

Use the following geometry for analysis, documentation, and future CAD input:

| Stage | Pinion | Gear | Module | Pressure angle | Ratio |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 18T | 80T | 1.5 mm | 20 degrees | 80/18 = 4.444444... |
| 2 | 18T | 81T | 1.5 mm | 20 degrees | 81/18 = 4.5 |

The total ratio is exactly 20:1. The linear motor-axis-to-output-axis distance
is 147.75 mm.

### Decision rationale

- Both stages use module 1.5 mm.
- The total reduction is exactly 20:1.
- Reduction is distributed close to evenly between the two stages.
- The largest outside diameter is 124.5 mm.
- The calculated 18T m1.5 motor-pinion HEX12 radial root wall is 4.697 mm.
- This is simpler and mechanically more conservative than mixed-module
  candidates.
- Candidate C does not justify m1.25 on the first stage.
- Candidate E provides only a small packaging benefit while requiring mixed
  modules.

### Consequences and limits

- The 18T motor pinion is geometrically above the theoretical 20 degree
  full-depth undercut threshold, but it remains the lower practical tooth-count
  boundary for an FDM nylon load path.
- A nylon strength decision requires measured motor load data and material/
  printing data; it has not been made.
- Do not create the motor-pinion CAD until `motor_hub_hex_axial_length` is
  measured.
- The HEX12 feature transmits torque. A stepped bore may transition from HEX12
  to clearance over the 11.5 mm body. The axial M4 and washer retain the
  pinion axially only; they do not carry primary drivetrain torque.

### Superseded geometric candidates

- C: `20T -> 90T m1.25; 18T -> 80T m1.5` is retained only as a study result,
  not the baseline.
- E: `21T -> 93T m1.25; 18T -> 81T m1.5` is retained only as a study result,
  not the baseline.
