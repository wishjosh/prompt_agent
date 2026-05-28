# Development Journal — Prompt Agent

> 현재형 요약 일지입니다. 전체 원문은 `archive/development_full_2026-05.md`에 보존합니다.

## 2026-05 — 연구 프롬프트군 구축과 코어-어댑터 전환

### 변곡점
- 디렉토리 아키텍처 정립: `prompts/`를 `research/`·`personal/`로 도메인 격리, 메타 문서를 `meta/`로 통합, `meta/catalog.md`(ID·목표 행위·AI 역할 F/CF·상태) 도입.
- 수집·해체·자산화 프롬프트 7종(v1.0) 일괄 설계 후 NotebookLM 전면 최적화(v1.1): 인용 마커 강제, "선택 소스 내에서만 답하라" 환각 차단, 탐색 단계의 Seed 문서 전략.
- 대규모 스캐닝 프롬프트 v1.2→v1.3(군집 5~6개 세분화 강제 + 토큰 한계 대응으로 대표 소스만 출력), `RES-000` ID를 파이프라인 순서로 재정렬(A=탐색 3종 / B=모드별 타겟팅 / C=교차 모드 종합), `test_results/` 신설.
- `RES-000-C`를 '간극 분석'에서 '입체적 종합'으로 재설계(투견장 모델 → 3D 퍼즐 모델).
- 단일 심층 해체를 소스 유형별로 세분화 합의(7종: A논문·B단행본보류·C보고서·D1/D2법령·E기사·G영상), `RES-002`→`RES-002-A` git mv 재명명, 영상 해체 `RES-002-G`를 v1.0(7섹션) → v2.0(멀티모드 deep/brief/recipe + 공통 척추)으로 재설계, 품질 게이트 `RES-000-D` 신설안 폐기.
- 저장소를 단일 파일 중심에서 **환경 중립 core + 환경별 adapters + NotebookLM 합본** 3계층으로 전환 착수, `RES-002-G` router/deep 분리, `build_notebooklm.ps1`→`build_notebooklm.py`.

### 현재 판단
- 프롬프트는 '맥가이버 칼'이 아니라 '메스'다. **결이 완전히 다르면 분리, 강도·분량만 다르면 모드**로 가른다(RES-000-A 1→3, RES-002 유형 분리, RES-002-G 멀티모드가 같은 원칙의 사례).
- 모든 프롬프트는 NotebookLM 구동 전제: 인용 마커 + grounded sources, 탐색은 Seed 문서 기반.
- 자산화 국면(`RES-003`/`RES-004`)에서 AI는 Facilitator가 아니라 Critical Friend — 🚨 Warning / Missing Links로 인지적 마찰을 극대화한다.
- 소스 품질 평가는 별도 게이트가 아니라 해체의 부산물로 드러낸다.

### 다음 작업
- 코어-어댑터 전환 마무리: `meta/catalog.md`의 기존 RES 링크를 실제 위치(`prompts/research/RES/`)와 정합화, `README.md` 디렉토리 설명을 `RES/`·`core/`·`adapters/`·`notebooklm/` 구조로 갱신.
- `RES-002-G` router/deep 파이프라인(NotebookLM 입력 길이 제약 대응) 마무리, brief/recipe 모드 어댑터 작성.
- 보류 항목 구체화: 단행본 `RES-002-B` 하이브리드 입력 양식, 법령 `RES-002-D1/D2`, 보고서 `RES-002-C` 시점 메타데이터.
