# Resume — Prompt Agent

## 현재 상태 (2026-06-06 갱신)
- 현재 구조: `principles/`, `guides/`, `prompts/`, `tests/`, `archive/`.
- 현재 연구 프롬프트는 `prompts/research/` 아래 6개 파일이다.
- 구 구조(`meta/`, `library/`, `packages/`, `lab/` 등)는 `archive/old_structure/`에 보존되어 있으며, 현재 실행 기준이 아니다.
- 현재형 저널 3종을 신설해 구 구조 아카이브와 현행 작업대를 분리했다.

## 바로 할 일
1. `research_agent`와 `event_agent`의 구 `prompt_agent/meta/*` 참조를 현재 구조에 맞게 정리한다.
2. `tests/runs/` 실행 기록과 프롬프트 상태 승격 기준을 다시 맞춘다.
3. `text_report_01_scan.md`, `text_report_02_deep.md` 등 최근 사용 프롬프트의 실패 기록을 `tests/`와 연결한다.

## 주의
- `archive/old_structure/` 아래 문서는 계보 확인용이다. 새 세션의 기본 기준으로 삼지 않는다.
- 검증 전에는 프롬프트를 코어/어댑터/빌드 구조로 나누지 않는다.
- 대규모 자동화보다 수동 실행 결과의 실패 패턴을 먼저 축적한다.
