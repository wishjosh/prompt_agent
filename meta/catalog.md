# 프롬프트 성능 현황판

> 이 파일은 "프롬프트 목록"이 아니라 성능 관리판이다. 새 프롬프트는 형식 등록보다 먼저 실제 입력으로 테스트한다.

## 상태 정의

- `draft`: 실행 가능한 초안. 아직 실제 결과 근거가 부족함.
- `trialed`: 실제 입력 1회 이상 실행함.
- `revised`: 테스트에서 드러난 실패나 한계를 반영해 수정함.
- `validated`: 서로 다른 입력 3개 이상에서 핵심 기준을 통과함.
- `stable`: 반복 사용 중인 표준 프롬프트.
- `legacy`: 분리 전 원본, 참고용 보존본, 또는 교체 예정본.

## 연구 도메인

> **파일명 체계**: `{도메인}_{단계}_{채널}_{세부유형}_{행위}` — 해체(digest) 계열 적용 완료. 수집(collect)·자산화(build) 계열은 추후 전환 예정.

### 수집 (collect) — 체계 미확정, 기존 ID 유지

| ID | 프롬프트명 | 현재 위치 | 상태 | 실행 근거 | 다음 실험 |
|----|-----------|----------|------|----------|----------|
| RES-000-A1 | [사회 인식 탐색 전략](../lab/experiments/research/RES/RES-000-A1_social_perception_exploration.md) | lab | draft | 없음 | Seed 문서 2종으로 키워드·커뮤니티 추천 품질 확인 |
| RES-000-A2 | [학술 이론 탐색 전략](../lab/experiments/research/RES/RES-000-A2_academic_theory_exploration.md) | lab | draft | 없음 | 논문 Seed 2종으로 이론 렌즈·검색어 품질 확인 |
| RES-000-A3 | [정책 현실 탐색 전략](../lab/experiments/research/RES/RES-000-A3_policy_reality_exploration.md) | lab | draft | 없음 | 법정계획/정책보고서 Seed로 행정 용어 변환 확인 |
| RES-000-B | [모드별 타겟팅 필터](../lab/experiments/research/RES/RES-000-B_mode_specific_filter.md) | lab | draft | 없음 | 혼합 소스 20개 내외로 모드 부합성 분류 확인 |
| RES-000-C | [교차 모드 입체 종합](../lab/experiments/research/RES/RES-000-C_multi_dimensional_synthesis.md) | lab | draft | 없음 | 사회·학술·정책 산출물 1세트로 사각지대 보완 확인 |

### 해체 (digest)

| ID | 구 ID | 프롬프트명 | 현재 위치 | 상태 | 실행 근거 | 다음 실험 |
|----|-------|-----------|----------|------|----------|----------|
| res_digest_multi_scan | RES-001 | [다중 소스 스캐닝](../lab/experiments/research/RES/res_digest_multi_scan.md) | lab | revised | [277개 소스 실행](../eval/runs/20260518_multi_source_scanning_v1.3_277개소스.md), [군집 A 세분화](../eval/runs/20260518_multi_source_scanning_v1.3_군집A_세분화.md) | 다른 주제의 50~100개 소스로 누락·군집 과대화 재검증 |
| res_digest_text_paper_deep | RES-002-A | [학술 논문 심층 해체](../lab/experiments/research/RES/res_digest_text_paper_deep.md) | lab | draft | 없음 | IMRaD 논문 1편 + 비정형 논문 1편으로 구조 적합성 확인 |
| res_digest_text_report_scan | RES-002-C-scan | [보고서 1차 스캔](../packages/notebooklm/research/core/res_digest_text_report_scan.md) / [어댑터](../packages/notebooklm/research/adapters/res_digest_text_report_scan.notebooklm.md) / [빌드](../packages/notebooklm/research/builds/res_digest_text_report_scan.notebooklm.md) | package | revised | [수원시 도시공간의 역사 1차 스캔](../eval/runs/20260529_RES-002-C-scan_v1.1_수원시도시공간의역사.md) | 법정계획서/정책보고서 각각 1개로 장르 차이 검증 |
| res_digest_text_report_deep | RES-002-C-deep | [보고서 2차 심층 해체](../packages/notebooklm/research/core/res_digest_text_report_deep.md) / [어댑터](../packages/notebooklm/research/adapters/res_digest_text_report_deep.notebooklm.md) / [빌드](../packages/notebooklm/research/builds/res_digest_text_report_deep.notebooklm.md) | package | revised | [수원시 도시공간의 역사 2차 심층 해체](../eval/runs/20260529_RES-002-C-deep_v1.0_수원시도시공간의역사_1부1-2장.md) | 스캔 맥락 임베드 방식으로 재실행 후 품질 비교 |
| res_digest_video_route | RES-002-G-router | [영상 모드 판별기](../packages/notebooklm/research/core/res_digest_video_route.md) / [어댑터](../packages/notebooklm/research/adapters/res_digest_video_route.notebooklm.md) / [빌드](../packages/notebooklm/research/builds/res_digest_video_route.notebooklm.md) | package | trialed | 영상 실사용 검증 기록은 journal에만 있음 | 짧고 밀도 높은 영상, 반응 영상, 튜토리얼 영상으로 라우팅 정확도 확인 |
| res_digest_video_deep | RES-002-G-deep | [영상 심층 해체](../packages/notebooklm/research/core/res_digest_video_deep.md) / [어댑터](../packages/notebooklm/research/adapters/res_digest_video_deep.notebooklm.md) / [빌드](../packages/notebooklm/research/builds/res_digest_video_deep.notebooklm.md) | package | trialed | 영상 실사용 검증 기록은 journal에만 있음 | 다중 화자 영상과 짧은 고밀도 강연으로 deep 구조 검증 |
| res_digest_video_legacy | RES-002-G | [영상 멀티모드 해체 (원본)](../packages/notebooklm/research/core/res_digest_video_legacy.md) | package | legacy | router/deep 분리 전 원본 | brief/recipe 분리 완료 후 유지 여부 결정 |

### 자산화 (build) — 체계 미확정, 기존 ID 유지

| ID | 프롬프트명 | 현재 위치 | 상태 | 실행 근거 | 다음 실험 |
|----|-----------|----------|------|----------|----------|
| RES-003 | [논리적 결합](../lab/experiments/research/RES/RES-003_logic_fitting.md) | lab | draft | 없음 | 실제 인용 후보 5개로 체리피킹·논리 비약 포착 확인 |
| RES-004 | [창조적 스파크](../lab/experiments/research/RES/RES-004_action_fitting.md) | lab | draft | 없음 | 해체 산출물 2개에서 연구 씨앗 전환 품질 확인 |

## 아키텍처 문서

> 실행 가능한 프롬프트가 아닌 설계 원칙·지침 및 구조 문서. 성능 상태(draft/validated 등) 적용 없음.

| 파일 | 위치 | 내용 | 최종 수정 |
|------|------|------|----------|
| [소스 수집 파이프라인](SOURCE_INGESTION_PIPELINE.md) | meta | 소스 입력 채널(말/글/영상/경험)의 2층위 처리 아키텍처. Layer 1 인식론적 태그(DIRECT/MEDIATED) + Layer 2 매체 라우팅(TEXTUAL/ACOUSTIC/MULTIMODAL). `KNOWLEDGE_SYSTEM` 파생 지침 | 2026-05-31 |
| [프롬프트 작성 지침](PROMPT_DRAFTING_GUIDE.md) | meta | `DESIGN_PRINCIPLES` 파생 *작성* 지침. 원칙별 작성 규칙(정방향·역방향 링크) + 작성 체크리스트. 포장은 `CORE_ADAPTER` 소관 | 2026-05-31 |

---

## 개인 도메인

| ID | 프롬프트명 | 현재 위치 | 상태 | 실행 근거 | 다음 실험 |
|----|-----------|----------|------|----------|----------|
| PER-001 | [사주 행동 분석](../lab/experiments/personal/prompts/BaZi%20Behavioral%20Analysis.md) | lab | draft | 없음 | 서로 다른 입력 3개로 일반론 회귀 여부 확인 |
