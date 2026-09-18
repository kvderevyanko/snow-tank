# Measurements and data register

Values are deliberately classified by source. A project-provided value is not
treated as measured or manufacturer data until its source is recorded.

## MEASURED

No physical dimensions have been recorded yet.

The owner reports possession of many `688-2RS` bearings (nominal `8 x 16 x
5 mm`), approximately ten `6001` bearings (nominal `12 x 28 x 8 mm`), and
bearings measured only as approximately `22 mm` OD by `6 mm` width. The last
item's bore has **not** been measured and its marking has not been recorded;
it is therefore named `bearing_22xTBDx6`, not 6900.

## MANUFACTURER/SELLER DATA

No motor or adapter catalogue data has been verified and recorded yet.

## CALCULATED

These values are reproduced by `python3 scripts/gearbox_geometry.py` using a
20 degree, standard full-depth spur profile without profile shift.

| Item | Value |
| --- | ---: |
| Stage 1 ratio | 4.444444...:1 |
| Stage 2 ratio | 4.5:1 |
| Total ratio | exactly 20:1 |
| Stage 1 pitch diameters, 18T / 80T | 27.0 / 120.0 mm |
| Stage 1 outside diameters, 18T / 80T | 30.0 / 123.0 mm |
| Stage 1 center distance | 73.5 mm |
| Stage 2 pitch diameters, 18T / 81T | 27.0 / 121.5 mm |
| Stage 2 outside diameters, 18T / 81T | 30.0 / 124.5 mm |
| Stage 2 center distance | 74.25 mm |
| Linear motor-axis to output-axis distance | 147.75 mm |
| 18T m1.5 root diameter | 23.25 mm |
| HEX12 corner to 18T m1.5 root-circle radial wall | 4.697 mm |
| M3 clearance-bore calculation value | 3.2 mm (parameter; print fit TBD) |
| Ø8 / Ø3.2 annular radial wall, I, J | 2.400 mm; 195.915 mm⁴; 391.829 mm⁴ |
| Ø10 / Ø3.2 annular radial wall, I, J | 3.400 mm; 485.727 mm⁴; 971.453 mm⁴ |
| Ø12 / Ø3.2 annular radial wall, I, J | 4.400 mm; 1012.729 mm⁴; 2025.458 mm⁴ |
| Ø10 versus Ø8 I/J ratio with Ø3.2 bore | 2.479× |

## TBD

- `motor_hub_hex_axial_length`: **critical; unknown.** Do not infer it from a
  photograph. Measure it on the actual brass adapter before motor-pinion CAD.
- Exact 775 model, operating voltage, speed-torque curve, stall torque, stall
  current, continuous rating, and front-bearing radial-load allowance.
- Brass-adapter source classification and physical verification of: 5 mm bore,
  18 mm overall length, 11.5 mm body diameter, HEX12 across flats, axial M4,
  and radial M4.
- Gear face widths, compound-shaft diameter, bearings, bearing locations,
  housing stiffness, backlash, and axial retention.
- Inner bore and marking of `bearing_22xTBDx6`; only after physical
  confirmation of `10 mm` bore or `6900` marking may it be called `6900`.
- Actual dimensions, seals, clearance and load rating of the available 6001
  bearings and 688-2RS bearings.
- Nylon grade, dry/conditioned state, printing parameters, tooth accuracy,
  lubrication, temperature, and required duty cycle.
- ESC current limits, reverse/braking behavior, battery voltage under load,
  sprocket pitch radius, vehicle load, and stall/shock cases.
