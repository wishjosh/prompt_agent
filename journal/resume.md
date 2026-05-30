# Resume — Prompt Agent

## 현재 상태

### 저장소 구조
- 중심축: `lab/` 실험 → `eval/` 검증 → `library/` 승격 → `packages/` 포장.
- 코어-어댑터 분리는 초안 작성 규칙이 아니라 검증 후 포장 규칙이다.

### 파일명 체계 (2026-05-30 전환)
- **해체(digest) 계열**: `{도메인}_{단계}_{채널}_{세부유형}_{행위}` 체계로 전환 완료.
  - 예: `RES-002-C-scan` → `res_digest_text_report_scan`
- **수집(collect)·자산화(build) 계열**: 체계 미확정, 기존 `RES-000` / `RES-003/004` ID 유지.
- 구 ID와 신 ID 대조표는 `meta/catalog.md` 해체 섹션의 "구 ID" 컬럼 참조.

### 소스 수집 파이프라인 아키텍처 (2026-05-30 신설)
- 문서 위치: `meta/SOURCE_INGESTION_PIPELINE.md`
- **Layer 1** — 인식론적 태그(라우팅 아님): `[DIRECT]` 직접지 / `[MEDIATED]` 매개지
- **Layer 2** — 매체 라우팅: `[TEXTUAL]` / `[ACOUSTIC]` / `[MULTIMODAL]`
- 경험/목격(`[DIRECT]`)은 독립 처리 경로 없음. 연구자가 글·말로 변환 후 Layer 2 진입.
- MULTIMODAL 채널의 분리 처리 후 재합산 방법은 미결(TBD).

### 원칙/지침 층위와 두 트랙 (2026-05-31 정립)
- **원칙 = 방향, 지침 = 현재 지형에서 방향을 유지하는 방법.** 라우팅·전처리 같은 운영 규칙은 지침이다.
- **지식 트랙**: `KNOWLEDGE_SYSTEM`(원칙) → `SOURCE_INGESTION_PIPELINE`(지침).
- **프롬프트 트랙**: `DESIGN_PRINCIPLES`(원칙) → `PROMPT_DRAFTING_GUIDE`(작성 지침) / `CORE_ADAPTER_ARCHITECTURE`(포장 지침).
- `PROMPT_DRAFTING_GUIDE`는 골격 상태. 각 규칙에 정방향·역방향 링크. §1을 실제 프롬프트 문구로 채우는 일은 `lab/` 실험과 함께 진행.

---

## 현재 성능 판단

| ID | 구 ID | 상태 | 근거 |
|----|-------|------|------|
| `res_digest_multi_scan` | RES-001 | revised | 277개 소스 실행 2건. `eval/runs/` 보유. |
| `res_digest_text_report_scan` | RES-002-C-scan | revised | 수원시 보고서 실사용 결과 보유. |
| `res_digest_text_report_deep` | RES-002-C-deep | revised | 수원시 보고서 실사용 결과 보유. |
| `res_digest_video_route` | RES-002-G-router | trialed | 영상 실사용 검증 기록 journal에만 있음. `eval/runs/` 파일화 필요. |
| `res_digest_video_deep` | RES-002-G-deep | trialed | 동일. |
| `res_digest_video_legacy` | RES-002-G | legacy | router/deep 분리 전 원본. 참고용. |
| `res_digest_text_paper_deep` | RES-002-A | draft | 실제 입력 테스트 없음. |
| RES-000-A1/A2/A3 | — | draft | 실제 입력 테스트 없음. |
| RES-000-B/C | — | draft | 실제 입력 테스트 없음. |
| RES-003/004 | — | draft | 실제 입력 테스트 없음. |

---

## 바로 할 일

1. `res_digest_video_route/deep` 영상 테스트 결과를 `eval/runs/` 형식으로 파일화.
2. `res_digest_text_report_scan/deep`을 법정계획서·정책보고서로 재검증 (수원시 보고서 외 장르).
3. `RES-000-A1/A2/A3` Seed 문서 테스트로 탐색 프롬프트 성능 근거 확보.
4. `RES-003/004` 자산화 프롬프트를 실제 해체 산출물에 연결해 테스트.
5. 수집(collect)·자산화(build) 계열 파일명 체계 확정.
6. MULTIMODAL 채널 재합산 방법 설계 (`meta/SOURCE_INGESTION_PIPELINE.md` TBD 항목).
7. `PROMPT_DRAFTING_GUIDE.md` §1을 lab 실험을 통해 실제 작성 규칙 문구로 채우기.

---

## 주의

- 합본(`packages/notebooklm/research/builds/`)은 파생물이므로 직접 수정하지 않는다.
- `eval/runs/` 파일명은 과거 기록 보존용이므로 구 ID가 남아 있어도 변경하지 않는다.
- 품질 게이트(`RES-000-D`류) cross-cutting 필터는 "옥상옥"으로 폐기됨. 재제안하지 않는다.
- 특화(sub-prompt) → 통합 전환은 AI 능력이 충분히 발전하는 시점까지 보류한다.
- 작성 지침의 새 규칙은 두 시험을 통과해야 한다(정방향: 어느 방향 유지 / 역방향: 실패 시 어느 원칙 의심). 원칙 수정은 단발이 아닌 eval 누적 추세 + 연구자 결정으로만.
- Shannon 엔트로피와 의미론적 밀도(정보 밀도) 혼용에 주의. 이 프로젝트에서 반복 발생하는 오류 패턴이다.
