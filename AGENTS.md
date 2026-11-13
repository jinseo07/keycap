# KEY / HOLD · 개발 하네스 지침

## 반복 개발 루프
요청된 변경마다 아래 순서로 작업한다.

1. 현재 구현과 이 파일의 완료 기준을 읽고, 바꿀 범위를 정한다.
2. 한 번에 한 가지 사용자 경험 변경을 구현한다.
3. 브라우저에서 실행해 영향받은 조작을 확인한다.
4. 오류나 기준 미달이 있으면 수정하고 다시 확인한다.
5. 완료 기준을 만족하면 멈추고, 확인하지 못한 항목은 분명히 보고한다.

## 게임 기준
- 게임은 누르기, 유지하기, 놓기 순서를 고민하는 5단계 키보드 논리 퍼즐이다.
- 단계는 점진적으로 어려워지며 시간 제한이나 빠른 타이핑을 요구하지 않는다.
- 동시 입력은 최대 열 키로 제한한다.
- 화면 키캡과 물리 키보드 입력을 지원한다.
- 자동화 하네스는 브라우저의 `window.__KEYCAP__` API를 사용하고, 게임과 동일한 입력 규칙을 통과한다.
- 키보드 유령 입력에 의존하지 않으며, 입력 실패 후 상태를 보존한다.
- 반응형 레이아웃과 어두운 키보드 중심 디자인을 유지한다.

## Harness API
- `press(key)`, `release(key)`: 게임 규칙을 통과하는 키 입력
- `restart()`: 현재 단계 초기화
- `selectStage(number)`: 해금된 단계 선택
- `state()`: 현재 단계, 눌린 키, 행동 수, 완료 상태 반환
- `stages()`: 단계 목표와 입력 규칙 반환


## Fresh-agent playtest loop

Run this loop only when the user asks for a game QA/playtest loop.

1. Start or refresh the actual game build in a browser. Prefer the local repository preview; exercise the real interface, not only source inspection or the harness API.
2. Spawn a new, independent tester agent for this round. Give it the current URL, the five-stage goal, device/viewport, and a request to play every stage from a clean state. Do not give it previous-round findings or a suggested answer. Ask it not to edit files.
3. Require the tester to report reproducible findings with severity, exact steps, expected and actual result, and evidence. Ask separately for one high-confidence usability improvement. Mark unverified assumptions clearly.
4. Triage findings. Fix reproducible blockers, incorrect state/solution behavior, and clear usability problems. Skip subjective polish unless it materially improves play.
5. Re-run the affected interaction yourself, then ask a different fresh tester to play the changed build.

## Stability and stop conditions

- Stop early only after two consecutive fresh testers independently complete all five stages and report no reproducible correctness issue or high-value usability improvement.
- Limit a run to six rounds. If meaningful findings remain at the limit, stop and report them as unresolved; do not claim stability.
- If a browser or fresh-agent tool is unavailable, do not claim a playtest pass. State what could not be exercised and continue only with checks that are actually possible.
- End with a short report of rounds run, findings fixed, actual play evidence, remaining issues, and why the loop stopped.

## 보고
각 반복 후 변경 파일, 실제로 실행해 확인한 조작, 남은 문제를 요약한다. 수행하지 않은 검증을 완료했다고 말하지 않는다.
