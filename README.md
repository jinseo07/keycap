# KEY / HOLD

KEY / HOLD는 단계별 시작 조합을 누른 채 지정된 순서의 새 키를 하나씩 누르고, 매번 기존 키 하나를 골라 놓아 마지막 목표 조합을 만드는 5단계 키보드 퍼즐입니다. 시작 조합, 전체 입력 순서, 현재 차례, 마지막 조합이 화면에 표시됩니다. 1단계는 한 키, 2단계는 두 키, 3~5단계는 세 키를 유지하며 새 키를 누르는 순간에는 한 키가 더 겹칩니다. 새 키는 유지해야 합니다. 잘못된 입력이나 목표에 도달할 수 없는 선택은 진행을 초기화합니다. 모든 키를 놓은 뒤 다시 시작하세요. 퍼즐 입력은 실제 키보드만 사용합니다. 힌트는 선택적으로 열 수 있으며 시간 제한은 없습니다.

## 로컬에서 실행
`index.html`을 브라우저에서 열거나 저장소 루트에서 정적 서버를 실행하세요.

```sh
python -m http.server 4173
```

브라우저에서 `http://localhost:4173`을 엽니다.

## Harness 루프
실행 중인 게임 탭에서 브라우저 개발자 도구 Console을 열고 `window.__KEYCAP__` API를 호출하세요. Harness 입력은 실제 키보드와 같은 시작 조합, 키 유지/해제 조건, 초기화 규칙을 따릅니다.

```js
__KEYCAP__.restart();
__KEYCAP__.press("F");
__KEYCAP__.press("D"); // F와 D가 잠시 함께 눌림
__KEYCAP__.release("F"); // 목표 조합 도달
__KEYCAP__.state();
```

API는 `press(key)`, `release(key)`, `restart()`, `selectStage(number)`, `state()`, `stages()`를 제공합니다. 반복 개발 규칙은 [AGENTS.md](AGENTS.md)에 있습니다.
