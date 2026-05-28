# Resume — Prompt Agent

## 현재 상태
- 메타 문서: `meta/DESIGN_PRINCIPLES.md`, `meta/KNOWLEDGE_SYSTEM.md`, `meta/CORE_ADAPTER_ARCHITECTURE.md`, 카탈로그 `meta/catalog.md`.
- 수집(`RES-000-A1/A2/A3`, `B`, `C`) · 해체(`RES-001`, `RES-002-A`) · 자산화(`RES-003`, `RES-004`) 프롬프트 작성 완료.
- 영상 해체 `RES-002-G` v2.0(멀티모드 deep/brief/recipe + 공통 척추) 완성, router/deep 분리 진행 중 (brief/recipe 미완).
- 저장소를 환경 중립 `core/` + 환경별 `adapters/` + `notebooklm/` 합본 3계층으로 전환 중 (`build_notebooklm.py`).

## 바로 할 일
1. `RES-002-G` router/deep 파이프라인 마무리 + brief/recipe 모드 어댑터 작성.
2. `meta/catalog.md`의 기존 RES 링크를 실제 위치(`prompts/research/RES/`)와 정합화.
3. `README.md` 디렉토리 구조 설명을 `RES/`·`core/`·`adapters/`·`notebooklm/` 구조로 갱신.

## 주의
- 상세 변경 이력은 `journal/archive/development_full_2026-05.md`와 `journal/archive/dialogue_full_2026-05.md`에 있다.
- NotebookLM 합본은 `core/` + `adapters/`에서 `build_notebooklm.py`로 생성한다 — **합본(`notebooklm/`) 파일을 직접 수정하지 않는다.**
- 품질 게이트(`RES-000-D`)류 cross-cutting 필터는 "옥상옥"으로 폐기됨 — 재제안하지 않는다.
- 특화(sub-prompt) → 통합 전환은 AI 능력이 충분히 발전하는 시점까지 보류한다.
