# TutorBridge - Stakeholder Validation Guide

Owner: Toprak Daldal. Status: prepared questions and tasks only, 19 November 2026. No new session, participant response, approval or measured result is claimed. Related: [SRS](SRS.md), [requirements task #59](https://github.com/Sprint-1-Software-engineering/Sprint-1/issues/59).

## Existing evidence

The team's reported 3 November conversation with one mathematics/software tutor is summarized in SRS section 1. It supports investigating coordination and homework-message organization; it does not measure prevalence or prove usability/adoption.

## Preparation

Use the actual Figma prototype when available; label it a prototype. Ask a consenting private tutor and, where appropriate, a student to review their own role. Use synthetic names, lesson times and homework. Do not collect private conversations, real student files or contact information for a public repository. Participants may decline or stop. No fixed sample count is asserted as a course requirement.

Record the real date, anonymous participant code/role, prototype version/link and facilitator only after a session occurs. Explain that there is no implemented video, payment, AI or parent feature.

## Questions

1. How are lesson times and homework arranged today? Ask for a recent concrete example rather than suggesting that the tool already solves it.
2. Which part requires repeated coordination, and what is its consequence? Record frequency/time only if the person actually provides it; otherwise mark unmeasured.
3. Does teacher approval of a student request fit the tutor's practice? What cancellation rule would they expect?
4. Is a teacher-shared invitation code acceptable? What would make it confusing?
5. Can the person explain who may read a homework file? Is the proposed file-sharing flow useful?
6. What is missing or unnecessary in the proposed screens? Distinguish a request from an agreed MVP change.

## Prototype tasks

| Task | Starting condition | Observe | Requirement links |
|---|---|---|---|
| Student requests a lesson | Signed in, connected teacher, future slot | Completion without intervention, time, confusion and understanding of pending state | FR-07, FR-09, FR-11 |
| Teacher decides a request | Teacher role, pending request | Correct decision path, understanding of approval/conflict/cancellation | FR-10, FR-12 |
| Teacher shares and student finds homework | Connected accounts and synthetic permitted file | Assignment target clarity, finding/download path and ownership understanding | FR-13, FR-14 |

Two minutes for the first task is the initial product target, not a passed result. Do not time an API call and report it as human task completion. Record assistance and failure as well as success.

## Recording and follow-up

After an actual session, record anonymous role/date/version, task outcome, observed time if measured, assistance, concrete feedback and limitations. Use paraphrases unless an exact quote was genuinely recorded. Link each resulting decision or change request to its FR/Story; an opinion is not automatically an accepted requirement.

Before a session exists, keep its result as not conducted. Do not fill a result template with invented participants, quotes, dates, timings or approval. One interview cannot establish broad demand.
