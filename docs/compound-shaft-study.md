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

## C — printed rotating journals in sidewall bearings (new study)

**Status: geometry/assembly direction only; NOT strength approved.** This
section supersedes the prior conditional preference for rotating steel shaft B
as the direction being investigated. It does not claim that a printed nylon
journal is strength- or life-approved.

### Hardware classification

| Name in this project | Nominal dimensions | Classification | Constraint |
| --- | ---: | --- | --- |
| 688-2RS | 8 x 16 x 5 mm | owner-provided nominal hardware | C1 uses its Ø8 inner race |
| `bearing_22xTBDx6` | `TBD x ~22 x ~6 mm` | owner observation only | Never call it 6900 until bore is measured as Ø10 or marking confirms 6900 |
| 6001 | 12 x 28 x 8 mm | owner-provided nominal hardware | seals, clearance and rating TBD |

M3 passes through a clearance bore (calculation parameter Ø3.2 mm; final
printed value TBD). It is a safety/tie and possible independently controlled
axial-retention member, never the primary torque path. Monolithic nylon carries
torque between the 80T and 18T portions of the compound and through the output
shaft/sprocket interface.

### Exact journal-section comparison

For annular journal outer diameter `D` and M3 clearance bore `d`:

\[
I={\pi\over64}(D^4-d^4),\quad J=2I,\quad Z={I\over D/2}
\]

`I`, `J`, and `Z` are geometric properties only; they do not approve nylon
strength, layer adhesion, root stress concentration, creep or fatigue.

| Journal / bore | radial nylon wall | I (mm⁴) | J (mm⁴) | Z (mm³) |
| --- | ---: | ---: | ---: | ---: |
| C1 Ø8 / Ø3.2 | 2.400 mm | 195.915 | 391.829 | 48.979 |
| C1 Ø8 / Ø3.3 | 2.350 mm | 195.241 | 390.481 | 48.810 |
| C2 Ø10 / Ø3.2 | 3.400 mm | 485.727 | 971.453 | 97.145 |
| C2 Ø10 / Ø3.3 | 3.350 mm | 485.052 | 970.105 | 97.010 |
| output Ø12 / Ø3.2 | 4.400 mm | 1012.729 | 2025.458 | 168.788 |

With Ø3.2 bore, C2 has 2.479× C1's `I` and `J`, and 1.983× C1's bending
section modulus. The bore itself reduces `I/J` relative to solid stock by
2.56% at Ø8, 1.05% at Ø10, and 0.51% at Ø12. The larger practical risk is the
printed journal-to-hub root and bearing-race fit, rather than the M3 hole.

### Load relationships and bearing support

Let `T_m` be motor torque in N m and `eta_1`, `eta_2` stage efficiencies. At
20-degree pressure angle:

\[
F_{t1}=74.074T_m,\quad F_{r1}=26.960T_m
\]
\[
T_c=4.444\eta_1T_m,\quad F_{t2}=329.218\eta_1T_m,
\quad F_{r2}=119.825\eta_1T_m
\]
\[
T_{out}=20\eta_1\eta_2T_m
\]

The second mesh is the dominant compound load. For bearing centre planes
`x=0,L` and radial mesh-resultant vectors `q1,q2` at `a1,a2`, calculate each
radial plane independently:

\[
R_B={q_1a_1+q_2a_2\over L},\qquad R_A=q_1+q_2-R_B
\]

Keep both mesh planes between those supports where possible; otherwise
minimize the second-stage overhang `e`. Its first-order journal-root moment is
`M_root ~= F_n2 e`; broad continuous journal-to-hub fillets are mandatory,
with final radius set only after axial geometry is known. A third bearing is
not a default improvement: FDM positional errors make it an over-constrained,
uncertain load-sharing system that can bind during assembly. Two correctly
spaced bearings are preferred.

### C1 versus C2 conclusion

| Criterion | C1: 2 x 688 / Ø8 journal | C2: 2 x `bearing_22xTBDx6` / Ø10 only when confirmed |
| --- | --- | --- |
| Confirmed hardware interface | Yes, nominally | No; bore is TBD |
| Journal geometric margin | Lower | Higher: 3.4 mm wall and 2.479× I/J |
| Housing envelope | smaller 16 mm OD bearing | approximately 22 mm OD bearing |
| Packaging direction | parameterized fallback | conditional preference |

Thus C2 is preferred **conditionally** after physical confirmation of a 10 mm
bore / 6900 marking. C1 is the physically identified fallback. Final journal
diameters stay unfrozen pending fit coupons.

### Output shaft and removable sprocket

Use two nominal 6001 supports: one near the 81T mesh plane, then the maximum
practical useful span, then one close to the sprocket. Minimize both gear and
sprocket overhangs. For gear load `G` at left overhang `e_g`, sprocket radial
load `S` at right overhang `e_s`, and span `L_o`:

\[
R_B=S(1+e_s/L_o)-G e_g/L_o,\qquad
R_A=G(1+e_g/L_o)-S e_s/L_o
\]

Track radial load must be determined from actual tension/preload and geometry;
it cannot be inferred from output torque alone. Sprocket tangential force is
`F_s = 20,000 eta_1 eta_2 T_m / r_s[mm]` N.

| Interface | torque radius | radial material from Ø3.2 bore to flats | assessment |
| --- | ---: | ---: | --- |
| HEX14 | 7.0 mm | 5.4 mm | preferred provisional package interface |
| HEX15 | 7.5 mm | 5.9 mm | retain as parametric intermediate |
| HEX17 | 8.5 mm | 6.9 mm | alternate; requires larger female hub and is not automatically better |

Use a male HEX14 on the monolithic output shaft, a lead-in and root fillets,
and an independent axial cap/retainer. The M3 may retain that cap but must not
be the torque path or clamp the two 6001 inner rings.

### FDM and service findings

- Bearing outer rings need sidewall shoulders plus removable bolted retainers;
  neither friction nor a snap feature alone is sufficient.
- A nylon journal needs a measured process/material-specific transition or
  light interference fit that prevents inner-ring spin. A nominal CAD press
  fit is not valid: nylon can creep, lose interference, fret and spin under
  reverse. A metal sleeve is a documented fallback if cycling fails, not part
  of this all-printed architecture.
- Print journal coupons at the actual production orientation. Face-flat gear
  printing gives tooth/face accuracy but makes journal axis build-Z; a
  horizontal-axis alternative improves journal fiber direction but harms
  supported surfaces and must be compared, not assumed.
- Print journals deliberately oversize, then light-sand/polish or turn their
  exterior to measured fit. Reaming is only appropriate for an internal bore.
- Make coupons for 8, 10 and 12 mm actual bearing IDs: axial M3 bore, real
  root fillet, lead-in and bearing-width engagement. Sweep external journal
  diameter around the *measured* bearing ID in 0.02 mm increments, initially
  across a ±0.06 mm screening range. Test dry, conditioned/wet and warm states
  for insertion/removal, runout, inner-ring spin, wear dust and reversing
  radial-load cycles. Test bearing OD pockets likewise with shoulder/retainer
  ring coupons.

### Packaging gate and remaining validation

The unknown motor torque does not block **parametric packaging CAD**. The
motor pinion remains a pitch/envelope placeholder until
`motor_hub_hex_axial_length` is measured. Packaging CAD must show insertion,
retainer access, removable sidewall sequence and no M3-induced bearing preload.

Strength approval is blocked by: actual bearing measurement/rating; nylon
grade, moisture state and print process; tooth widths and transition geometry;
motor/reverse/stall and track-tension loads; coupon fit/creep/fretting/reverse
evidence; and strength/fatigue validation of gear, root and sprocket interface.
