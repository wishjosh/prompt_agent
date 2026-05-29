# Resume — Prompt Agent

## 현재 상태
- 메타 문서: `meta/DESIGN_PRINCIPLES.md`, `meta/KNOWLEDGE_SYSTEM.md`, `meta/CORE_ADAPTER_ARCHITECTURE.md`, 카탈로그 `meta/catalog.md`.
- 수집(`RES-000-A1/A2/A3`, `B`, `C`) · 해체(`RES-001`, `RES-002-A`) · 자산화(`RES-003`, `RES-004`) 프롬프트 작성 완료.
- 영상 해체 `RES-002-G` v2.0(멀티모드 deep/brief/recipe + 공통 척추) 완성, router/deep 분리. **router v1.2 — 콘텐츠 개요(생산자 의도 기준) 추가 + 모드 기준에서 길이 제거(밀도·목적 중심)**. **router+deep tested(영상 검증).** brief/recipe 어댑터 미완.
- **보고서 해체 `RES-002-C` 신설**(scan/deep v1.1): `RES-002-C-scan`(1차) → `RES-002-C-deep`(2차). **첫 실사용 검증 완료**(수원시 도시공간의 역사 650p — `test_results/20260529_RES-002-C-*`). Studio 별개-파일 제약 대응(스캔 맥락을 deep 본문에 임베드) + 산출물 제목 규약(`1차 스캔_[제목]`/`2차 심층 해체_[제목] — [범위]`) 반영.
- **실행 채널**: 단일 소스 해체 → NotebookLM Studio "보고서 기능"; 다량 소스 스캐닝 → 채팅창.
- 저장소를 환경 중립 `core/` + 환경별 `adapters/` + `notebooklm/` 합본 3계층으로 전환 중 (`build_notebooklm.py`).

## 바로 할 일
1. `RES-002-C` 보고서 파이프라인을 실제 방대 소스로 1차 스캔→2차 심화 테스트.
2. `RES-002-G` brief/recipe 모드 어댑터 작성.
3. `meta/catalog.md` 기존 RES 링크를 `prompts/research/RES/`와 정합화 + `README.md` 디렉토리 구조 갱신.

## 주의
- 상세 변경 이력은 `journal/archive/development_full_2026-05.md`와 `journal/archive/dialogue_full_2026-05.md`에 있다.
- NotebookLM 합본은 `core/` + `adapters/`에서 `build_notebooklm.py`로 생성한다 — **합본(`notebooklm/`) 파일을 직접 수정하지 않는다.**
- 품질 게이트(`RES-000-D`)류 cross-cutting 필터는 "옥상옥"으로 폐기됨 — 재제안하지 않는다.
- 특화(sub-prompt) → 통합 전환은 AI 능력이 충분히 발전하는 시점까지 보류한다.
