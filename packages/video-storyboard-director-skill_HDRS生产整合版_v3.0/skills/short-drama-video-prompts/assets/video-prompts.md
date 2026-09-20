# Video Prompts Delivery Template

This document renders accepted motion specs into model-facing execution text. It is a delivery cache, not a second source of truth. Every paragraph must remain traceable to `motion-specs.jsonl`, accepted storyboard fields, asset bindings and exact dialogue/VO obligations.

## Delivery rules

- One shot, one primary action change.
- At most one secondary reaction.
- One primary camera intent.
- Dialogue and VO stay verbatim and keep their accepted relative order against actions.
- VO does not cause visible lip movement unless the character is actually speaking in-scene.
- Characters without dialogue remain naturally alive unless the shot explicitly requires stillness.
- Model-facing text contains only visible/audible execution content; no file paths, rule IDs, review notes, hashes or internal workflow labels.
- Continuity IN starts from the accepted storyboard start boundary; continuity OUT must land on the accepted storyboard end boundary.

## Shot template

```text
<shot id only in the human-facing heading, not inside the model-facing prompt>

<accepted starting visible state>. Because <event cue>, <primary action>. <optional secondary reaction>. Camera <single primary movement or locked intent>. <dialogue / VO / SFX only when accepted and needed>. End with <accepted terminal visible state>. Preserve <only the continuity facts that are easy to drift and needed by this shot>.
```

## Container note

When the creator uses multi-shot delivery containers, the container section only lists member shot order and summed accepted duration. It does not merge shot boundaries or create new story actions.
