# RC Snowcat Engineering Project

## Goal

Design a compact RC tracked vehicle capable of operating in deep loose snow.

The project must produce a mechanically realistic, printable, assembleable
design rather than only visually plausible CAD.

## Engineering workflow

Use specialist subagents when their domain is involved.

### drivetrain_engineer

Delegate to this agent before:
- changing gear tooth counts;
- changing module;
- changing drivetrain ratio;
- selecting shaft sizes;
- selecting drivetrain bearings;
- estimating torque or vehicle speed.

Its analysis should be independent of the current CAD.

### mechanical_designer

Use this agent to implement accepted mechanical decisions in CAD.

It may modify CAD files, but must not silently change engineering interfaces
or requirements.

### print_reviewer

Run this agent after creating or materially changing an FDM part.

Its review is mandatory for:
- gears;
- track links;
- sprockets;
- bearing housings;
- high-load nylon parts.

### design_reviewer

Run this agent as an independent gate after a subsystem reaches a candidate
state.

It must not modify the design being reviewed.

## Required sequence for major mechanical work

Engineering analysis
→ CAD implementation
→ FDM/manufacturing review
→ independent design gate
→ corrections
→ tests
→ user report.

Do not let the same specialist both create a design and provide the final
independent approval for that design.

## Project rules

- Never invent dimensions of purchased parts.
- Unknown values are TBD.
- Separate measured values, manufacturer values, assumptions, and calculations.
- Parametric source is authoritative; STL is generated output.
- Interface changes must be documented.
- Physical assembly must be verified, not inferred from collision-free CAD.
- Prefer simple reproducible calculations over opaque estimates.
- Run tools/test.sh after relevant changes.
- Do not commit unless the user explicitly requests a commit.
