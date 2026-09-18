# Two-stage 20:1 gearbox study

## Adopted geometry

This document records D-001, the **provisional geometric baseline**. It is not
a final, validated, or strength-approved drivetrain.

```text
motor: 18T m1.5 -> 80T m1.5 -- compound shaft -- 18T m1.5 -> 81T m1.5: output
                 4.444444...:1                                  4.5:1
```

The baseline uses standard 20 degree full-depth spur gears with no profile
shift. Module is 1.5 mm for both stages.

## Reproducible calculation

For module `m` and tooth count `z`:

\[
d=mz,\qquad d_a=m(z+2),\qquad d_f=m(z-2.5)
\]

For a gear pair:

\[
a=\frac{m(z_1+z_2)}2,\qquad i=\frac{z_2}{z_1}
\]

The HEX root-wall screening calculation is:

\[
t=\frac{d_f-D_{HEX,circumscribed}}2
\]

with `D_HEX,circumscribed = 13.856 mm`. Run:

```sh
python3 scripts/gearbox_geometry.py
```

| Parameter | Stage 1 | Stage 2 |
| --- | ---: | ---: |
| Teeth, pinion -> gear | 18 -> 80 | 18 -> 81 |
| Ratio | 4.444444... | 4.5 |
| Pitch diameter, pinion -> gear | 27.0 -> 120.0 mm | 27.0 -> 121.5 mm |
| Outside diameter, pinion -> gear | 30.0 -> 123.0 mm | 30.0 -> 124.5 mm |
| Root diameter, pinion -> gear | 23.25 -> 116.25 mm | 23.25 -> 117.75 mm |
| Center distance | 73.5 mm | 74.25 mm |

The total ratio is exactly `20:1`; linear motor-axis-to-output-axis distance
is `147.75 mm`. The motor 18T pinion root wall from the HEX12 corner to the
root circle is `4.697 mm`.

## Strength boundary

Geometry does not establish tooth or interface strength. Before a strength
decision, obtain the motor, ESC, nylon, printing, load, and adapter data listed
in [measurements.md](measurements.md). In particular, the axial depth of the
HEX12 drive is unknown. It controls nylon/HEX contact area, transferable torque,
the stepped motor-pinion bore, and allowable motor-pinion face width.

No CAD has been created for this study.
