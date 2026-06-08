# Development Journal — Prompt Agent

> 현재형 요약 일지입니다. 구 구조 원문은 `archive/old_structure/journal/`에 보존합니다.

## 2026-06 — 단순 프롬프트 작업대 구조로 재정리

### 2026-06-06 — 현재 구조와 저널 기준 정리

변곡점
- `prompt_agent`의 현재 운영 구조를 `principles/`, `guides/`, `prompts/`, `tests/`, `archive/` 중심으로 확인했다.
- 구 `meta/`, `library/`, `packages/`, `lab/`, `core/adapter/build` 중심 구조는 `archive/old_structure/` 아래 보존본으로 분리되어 있으며, 현재 실행 기준으로 보지 않는다.
- 현재형 저널 3종(`development.md`, `dialogue.md`, `resume.md`)을 신설해 구 구조 아카이브와 현행 작업대를 분리했다.
- 루트 [`../INDEX.md`](../INDEX.md)와 [`../JOURNAL_INDEX.md`](../JOURNAL_INDEX.md)에 현재 기준을 반영했다.

현재 판단
- 지금 단계의 핵심은 패키지화가 아니라 **프롬프트 파일 1개 단위의 수동 실행·기록·수정**이다.
- 실행 기록은 `tests/runs/`, 평가 기준은 `tests/`에서 관리한다.
- 오래된 실험은 삭제하지 않고 `archive/old_structure/`에 보존하되, 새 세션의 기본 진입점으로 쓰지 않는다.

다음 작업
- `research_agent`와 `event_agent`에 남아 있는 구 `prompt_agent/meta/*` 참조를 현재 `principles/`, `guides/`, `prompts/research/`, `tests/` 구조에 맞게 정리한다.
- 프롬프트 상태 기준을 현재 단순 상태(`draft`, `working draft`, `tested`, `stable`)와 `research_agent`의 도구 추천 기준 사이에서 다시 맞춘다.
- `tests/runs/`의 실행 기록과 실제 프롬프트 파일의 수정 이력을 연결하는 최소 규칙을 정한다.
