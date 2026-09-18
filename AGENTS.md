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

## Git and GitHub workflow

Remote repository: `https://github.com/kvderevyanko/snow-tank`

Commits and pushes are permitted when they follow this workflow.

1. Never push directly to `master` or `main` without a separate explicit user instruction.
2. Create a separate working branch for each substantial stage, named
   `codex/<short-task-name>` (for example, `codex/drivetrain-study`,
   `codex/gearbox-v1`, or `codex/track-v1`).
3. Before starting work, run `git status`, determine the current branch, check
   `origin`, confirm that it addresses the repository above, and run
   `git fetch origin`.
4. Never overwrite another contributor's history. Without separate permission,
   do not use `git push --force`, do not run `git reset --hard` on published
   history, and do not modify `master` or `main` directly.
5. Each commit must represent one logically complete engineering step.
6. Before committing:
   - run `tools/test.sh`;
   - inspect `git diff`;
   - confirm generated artifacts have not accidentally entered source control;
   - confirm temporary or debug files are absent.
7. Use short, technical commit messages, for example:
   `drivetrain: compare 20:1 gearbox candidates`,
   `cad: add parametric gearbox baseline`,
   `cad: add HEX12 motor pinion interface`,
   or `review: close gearbox assembly blockers`.
8. After a successful commit, push the working branch to `origin` and report:
   branch, commit SHA, concise contents, tests, known TBD values, and files
   that changed substantially.
9. Do not create a pull request unless the user explicitly requests one.
10. Do not merge a working branch into `master` or `main` independently.
