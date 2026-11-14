# KEY / HOLD

KEY / HOLD는 시작 키 조합 3개를 동시에 누르고, 정해진 순서로 누르거나 놓아 목표 키 조합 3개를 만드는 5단계 물리 키보드 논리 퍼즐입니다. 이동 중에는 최대 4개 키가 잠시 함께 눌릴 수 있습니다. 잘못된 입력을 하면 현재 퍼즐이 초기화되며, 모든 키를 놓은 다음 시작 조합을 다시 눌러야 합니다. 마우스는 퍼즐 입력에 사용하지 않고, 화면 키보드는 눌림 상태를 표시합니다. 시간 제한은 없습니다.

## 로컬에서 실행
`index.html`을 브라우저에서 열거나 저장소 루트에서 정적 서버를 실행하세요.

```sh
python -m http.server 4173
```

브라우저에서 `http://localhost:4173`을 엽니다.

## Harness 루프
실행 중인 게임 탭에서 브라우저 개발자 도구 Console을 열고 `window.__KEYCAP__` API를 호출하세요. Harness 입력은 실제 키보드와 같은 시작 조합, 누름/놓음 순서, 초기화 규칙을 따릅니다.

```js
__KEYCAP__.restart();
__KEYCAP__.press("F");
__KEYCAP__.press("J");
__KEYCAP__.press("K"); // 시작 조합을 잡아 퍼즐 시작
__KEYCAP__.press("D"); // 네 키가 잠시 눌림
__KEYCAP__.release("F"); // 목표 조합 도달
__KEYCAP__.state();
```

API는 `press(key)`, `release(key)`, `restart()`, `selectStage(number)`, `state()`, `stages()`를 제공합니다. 반복 개발 규칙은 [AGENTS.md](AGENTS.md)에 있습니다.
