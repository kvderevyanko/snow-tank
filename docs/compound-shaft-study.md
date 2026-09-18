# Compound shaft architecture study

## Status and scope

This is an independent, pre-CAD engineering comparison for the D-001 compound
gear: `80T m1.5 + 18T m1.5` on one axis. It does not select a shaft, bearing,
or final drivetrain design. CAD has not been created.

The 18T compound pinion has pitch/root/outside diameters of `27.0 / 23.25 /
30.0 mm`. Face widths, motor torque, material, and print process remain TBD.

## Calculated load relationships

Let `T_m` be motor torque in N m and `eta_1` be first-stage efficiency.

\[
F_{t1}=T_m/0.0135=74.07T_m\ \mathrm{N}
\]

\[
T_c=4.444\eta_1T_m,\qquad
F_{t2}=T_c/0.0135=329.22\eta_1T_m\ \mathrm{N}
\]

For 20 degree spur gears, `F_r = F_t tan(20 degrees) ~= 0.364 F_t`. The
second mesh is therefore the dominant radial and bending load source for the
compound assembly. These equations are not a strength approval because
`T_m`, `eta_1`, tooth widths, and shock cases are unknown.

## Candidate bearing envelope

The initial candidate is a 688-size bearing: `8 x 16 x 5 mm`. A concentric
16 mm outside-diameter bearing envelope inside the 18T root circle leaves:

\[
(23.25-16)/2=3.625\ \mathrm{mm}
\]

of nominal radial nylon. This number excludes root fillets, FDM tolerance,
seat interference, webs, moisture creep, local load concentration, and shock.
It is not evidence that a bearing seat under the 18T is sufficient.

Other standard dimensional candidates considered, subject to manufacturer
datasheet verification before purchase:

| Candidate | Nominal dimensions | Radial nylon to 18T root if concentric | Assessment |
| --- | ---: | ---: | --- |
| 688 | 8 x 16 x 5 mm | 3.625 mm | Compact candidate; requires proof of the nylon seat. |
| 698 | 8 x 19 x 6 mm | 2.125 mm | Not justified under 18T; could fit only in the 80T hub. |
| 608 | 8 x 22 x 7 mm | 0.625 mm | Not viable concentrically under 18T. |
| 687 | 7 x 14 x 5 mm | 4.625 mm | Needs a 7 mm shaft; shaft bending stiffness falls to about 0.586 of 8 mm. |
| 689 | 9 x 17 x 5 mm | 3.125 mm | Does not improve the 18T wall and changes the shaft interface. |

The 688-size envelope remains a reasonable study candidate, not a bearing
selection and not a claim about load rating or life.

## A — fixed 8 mm shaft; bearings inside compound gear

The steel shaft is fixed in the gearbox. The compound gear rotates on two
bearings; their inner rings remain stationary and their outer rings are seated
in nylon.

### Placement and load path

| Placement | Feasibility | Assessment |
| --- | --- | --- |
| Both 688 bearings in an enlarged 80T hub | Geometrically possible | Most credible A configuration, but 18T is overhung from the nearest support. |
| One bearing in 80T and one concentric under 18T | Formally possible | Not recommended without calculation and creep proof: only 3.625 mm nominal nylon remains. |
| One bearing at each compound-stack edge | Formally possible | Retains the same 18T bearing-seat concern. |

Two 5 mm-wide bearings placed directly adjacent provide only 5 mm
center-to-center span. An effective design must separate them positively and
place the nearest bearing as close as possible to the 18T mesh plane. If both
are inside 80T, the more heavily loaded 18T mesh remains a cantilever.

### Assessment

| Criterion | Assessment |
| --- | --- |
| Stiffness and bearing loads | Limited by internal bearing span and 18T overhang. |
| Nylon creep | Outer race can spin/fret and enlarge the printed seat after moisture and thermal cycles. |
| Torque transfer | Favorable: a monolithic printed compound transfers torque internally without a separate small-radius shaft interface. |
| Axial retention | Outer races require positive shoulders plus removable retainers; friction fit alone is insufficient. |
| Assembly/service | Moderate: one sidewall or retainer must be released to remove the compound from the fixed shaft. |
| Manufacturability | Favourable if a suitable precision 8 mm journal shaft is available; a threaded M8 bolt is not a bearing journal. |
| Reversing/shock | No separate shaft-drive interface, but seat creep and overhung 18T hub are critical risks. |

Expected failures: 18T seat cracking or creep if used; 80T-hub-to-18T fatigue
crack; outer-race spin; fixed-shaft deflection; axial movement from incomplete
retention; and compound-web damage during reverse/stall events.

## B — rotating steel shaft; bearings in gearbox sidewalls

The compound gear is positively connected to a rotating steel shaft. Two
bearings are seated in the gearbox sidewalls, with both gear planes arranged
between them where possible.

### Assessment

| Criterion | Assessment |
| --- | --- |
| Stiffness and bearing loads | Potentially superior: bearings can span the gearbox and directly support both mesh planes. |
| Nylon creep | No bearing seat is required in 18T. Sidewall seats can be made thicker and reinforced, but still need fit/creep validation. |
| Torque transfer | Primary unresolved risk. The interface must transmit `4.444 eta_1 T_m` in both directions. |
| Axial retention | Shaft shoulders/spacers/collars and sidewall retainers are needed. Spur gears have no design axial thrust, but vibration and reverse require positive retention. |
| Assembly/service | Potentially good: release one sidewall and remove shaft plus compound as a module. |
| Manufacturability | Depends on a real, repeatable steel shaft/hub interface; a complex custom shaft cannot be assumed. |
| Purchased parts | More than A: shaft, two bearings, retainers, and likely a metal hub plus its hardware. |
| Reversing/shock | Good support geometry, but the torque interface can become the first failure point. |

### Torque-interface screening

Neither a nylon friction fit nor a lone radial set screw is an acceptable
primary torque path: nylon creeps and the localized screw load damages the
hub. At an illustrative 4 mm effective interface radius:

\[
F_{interface}\approx\frac{4.444\eta_1T_m}{0.004}
=1111\eta_1T_m\ \mathrm{N}
\]

The interface must therefore be selected and checked independently of gear
tooth geometry.

| Interface | Screening assessment |
| --- | --- |
| D-flat plus set screw | Do not use as primary torque transfer. |
| Nylon clamp/friction | Do not use as primary torque transfer. |
| Cross-pin through shaft and printed hub | Study only; needs controlled drilling, weakens the shaft locally, and must sit in a reinforced 80T hub rather than 18T. |
| Keyed shaft plus keyed metal hub | Mechanically credible, but requires a purchasable or reproducibly manufactured keyed shaft/hub. |
| Hex/D-profile shaft with round journals | Positive transfer is possible, but requires accurately made journals or steel sleeves. |
| Metal flanged hub in 80T, positive shaft interface, bolted gear connection | Most credible B direction, but the exact standard hub, bolt circle, retention, and nylon reinforcement are TBD. |

Expected failures: nylon hub damage at a pin/key/flat; set-screw loosening;
hub crack at a bolt circle; shaft fatigue at a cross-hole/shoulder; axial stack
movement; sidewall seat damage; and additional backlash from interface motion.

## Comparison and recommendation

| Criterion | A: fixed shaft/internal bearings | B: rotating shaft/sidewall bearings |
| --- | --- | --- |
| Mesh support | Constrained by short internal span and likely 18T overhang | Better potential; both mesh planes can lie between bearings |
| 18T bearing seat | Required or 18T is cantilevered | Eliminated |
| Torque path | Simple monolithic nylon path | Requires a positive metal-to-nylon interface |
| Current implementation readiness | Higher, but has a load-path compromise | Lower, pending interface selection |
| Long-term robust potential | Moderate | Higher if the interface is proven |

**Conditional preference: B, rotating steel shaft with sidewall bearings.** It
offers the better support geometry for the more heavily loaded second mesh and
avoids an unproven bearing seat in the 18T pinion. It is not approved for CAD
until a positive, manufacturable, serviceable torque interface is selected.

If that interface cannot be sourced or made reproducibly, the fallback is A:
two bearings inside a reinforced 80T hub, a monolithic printed compound, no
bearing under 18T, and a deliberately minimized 18T overhang. That fallback
still requires strength and print review before CAD approval.

## BLOCKER/TBD before CAD

1. Specific 775 motor data: voltage, speed-torque curve, stall and continuous
   torque/current, and allowed front-bearing radial load.
2. Target gear face widths, axial stack, mesh-plane locations, sidewall envelope,
   and desired bearing span.
3. Nylon grade/state, print orientation and accuracy, creep evidence, and
   temperature/moisture range.
4. Datasheet and supply choice for the actual 688-size bearing: sealing,
   clearance, tolerances, load rating, lubricant, and temperature limits.
5. Reverse, stall, snow-ingress, and track-shock load cases plus a life and
   safety-factor criterion.
6. For B: a specific available positive torque interface, including steel
   hub/shaft geometry, manufacturable process, axial retention, and a
   calculation or physical proof of the nylon hub.
7. For A: bearing-seat tolerance, positive race retention, and proof testing
   against nylon creep/spin.
