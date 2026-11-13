# KEY / HOLD

키를 누르고, 유지하고, 놓는 순서를 푸는 5단계 논리 퍼즐입니다. 시간 제한 없이 화면 키캡 또는 물리 키보드로 플레이합니다. 동시 입력은 최대 두 키입니다.

## 로컬에서 실행
`index.html`을 브라우저에서 열거나 저장소 루트에서 정적 서버를 실행하세요.

```sh
python -m http.server 4173
```

브라우저에서 `http://localhost:4173`을 엽니다.

## Harness 루프
실행 중인 게임 탭에서 브라우저 개발자 도구 Console을 열고 `window.__KEYCAP__` API를 호출하세요. 게임 입력과 같은 규칙을 적용합니다.

```js
__KEYCAP__.restart();
__KEYCAP__.press("F");
__KEYCAP__.press("J");
__KEYCAP__.state();
```

API는 `press(key)`, `release(key)`, `restart()`, `selectStage(number)`, `state()`, `stages()`를 제공합니다. 반복 개발 규칙은 [AGENTS.md](AGENTS.md)에 있습니다.
