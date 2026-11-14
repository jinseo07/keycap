# KEY / HOLD · 개발 하네스 지침

## 반복 개발 루프
요청된 변경마다 아래 순서로 작업한다.

1. 현재 구현과 이 파일의 완료 기준을 읽고, 바꿀 범위를 정한다.
2. 한 번에 한 가지 사용자 경험 변경을 구현한다.
3. 브라우저에서 실행해 영향받은 조작을 확인한다.
4. 오류나 기준 미달이 있으면 수정하고 다시 확인한다.
5. 완료 기준을 만족하면 멈추고, 확인하지 못한 항목은 분명히 보고한다.

## 게임 기준
- 게임은 시작 키 3개를 동시에 누르고, 정해진 누름/놓음 순서로 목표 키 3개에 도달하는 5단계 물리 키보드 논리 퍼즐이다.
- 단계는 점진적으로 어려워지며 시간 제한이나 빠른 타이핑을 요구하지 않는다.
- 전환 중에는 최대 4개 키가 잠시 함께 눌릴 수 있다.
- 게임 입력은 실제 키보드만 사용하며, 화면 키보드는 눌림 상태를 표시한다.
- 잘못된 전이는 진행을 초기화한다. 눌린 키를 모두 놓은 뒤 시작 조합을 다시 입력해야 한다.
- 자동화 하네스는 브라우저의 `window.__KEYCAP__` API를 사용하고, 게임과 동일한 입력 규칙을 통과한다.
- 키보드 포커스 상실 시 유령 입력을 남기지 않고 현재 퍼즐을 초기화한다.
- 반응형 레이아웃과 어두운 키보드 중심 디자인을 유지한다.

## Harness API
- `press(key)`, `release(key)`: 게임 규칙을 통과하는 키 입력
- `restart()`: 현재 단계 초기화
- `selectStage(number)`: 해금된 단계 선택
- `state()`: 현재 단계, 눌린 키, 진행 단계, 완료/시작/초기화 대기 상태 반환
- `stages()`: 단계 시작 조합, 목표 조합, 입력 규칙, 중간 최대 눌림 수 반환


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
