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

## D-002 — printed rotating-journal architecture C, study outcome

**Status: conditional packaging direction; NOT strength approved.**

The compound `80T + 18T` and output `81T + output journal` may be represented
in first packaging CAD as monolithic nylon rotating parts with bearings seated
in gearbox sidewalls. M3 is an axial safety/tie member through clearance bore;
it is not a primary torque path and must not preload bearing inner rings.

- Conditional preferred compound configuration: C2, two `bearing_22xTBDx6`
  sidewall bearings and Ø10 journals **only if** bore is physically confirmed
  as 10 mm / bearing marked 6900.
- Confirmed fallback/configuration: C1, two 688-2RS sidewall bearings and Ø8
  journals. It remains packaging-valid but has less nylon/root/fit margin.
- Default output support: two nominal 6001 bearings, one near 81T and one near
  the removable sprocket, maximally separated within the housing. No third
  bearing without a demonstrated load-path advantage.
- Provisional sprocket interface: printed HEX14, with HEX17 retained as a
  parametric alternative. The final choice depends on the actual sprocket-core
  diameter, engagement length and reversal/shock proof.

These statements are geometry and assembly decisions only. Required physical
fit, creep, fatigue and load validation remains open in D-002's study record.
