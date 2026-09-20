# Review and fixtures

Use this file when checking the skill package or reviewing a generated prompt set.

## Review focus

1. Source truth is intact: dialogue, VO, relationship facts and causal order have not been rewritten.
2. Every prompt maps to one accepted shot and one accepted terminal state.
3. Continuity IN and OUT are explicit enough to prevent reinitialization.
4. The actor load is within one primary action plus at most one secondary reaction.
5. Camera movement has an event trigger and one main intent.
6. Voice identity is preserved and VO does not trigger lip sync.
7. Model-facing text is free from workflow prose and internal IDs except human-facing headings.

## Minimal fixture set

A useful regression fixture should include at least:

- a two-person confrontation with a clear left/right relationship;
- a prop handoff where ownership changes;
- a VO line over visible silent acting;
- a reaction beat shorter than 1.5 seconds;
- a shot whose accepted duration is over 3 seconds for a documented production reason;
- one continuity-sensitive wardrobe, wound or hand-held state.

## Production interpretation

Passing static checks proves package structure and prompt invariants only. It does not prove that an external video model generated usable footage. When no generation run has been performed, mark model performance as `TEST_REQUIRED` rather than "validated".
