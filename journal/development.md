# Development Journal — Prompt Agent

> 현재형 요약 일지입니다. 전체 원문은 `archive/development_full_2026-05.md`에 보존합니다.

## 2026-05 — 연구 프롬프트군 구축과 코어-어댑터 전환

### 변곡점

- 초기에는 `prompts/` 중심으로 연구/개인 도메인을 격리하고, `meta/catalog.md`에 ID·목표 행위·역할·상태를 등록하는 방식으로 출발했다.
- 수집·해체·자산화 프롬프트 7종을 일괄 설계한 뒤, NotebookLM 실행에 맞춰 인용 마커, 선택 소스 한정, Seed 문서 전략을 반영했다.
- 대규모 스캐닝 프롬프트는 실제 277개 소스 테스트를 통해 군집 과대화와 출력 토큰 한계를 발견했고, v1.3에서 세분화와 출력량을 조정했다.
- 단일 심층 해체는 소스 유형별로 세분화했다. 영상(`RES-002-G`)은 router→deep 파이프라인으로, 보고서(`RES-002-C`)는 scan→deep 파이프라인으로 분리했다.
- `RES-002-C`는 『70, 수원시 도시공간의 역사』 실사용에서 메타 진단, 구조 X-ray, 수치 불일치 포착, Secondary Fragment 보존이 작동함을 확인했다.
- 2026-05-30 전면 개편에서 저장소의 중심을 `lab/` 실험, `eval/` 검증, `library/` 승격, `packages/` 포장 구조로 바꿨다. 코어-어댑터는 초안 작성 규칙이 아니라 검증 후 포장 규칙으로 낮췄다. 기존 템플릿과 경로 대응표는 루트 `legacy/`로 보이게 분리했다.

### 현재 판단

- 프롬프트는 먼저 성능 실험의 대상이다. 재사용 모듈은 반복되는 성공/실패 패턴이 드러난 뒤 추출한다.
- "잘 작동한다"의 근거는 `eval/runs/`의 실제 실행 결과와 `eval/scorecard.md`의 기준으로 판단한다.
- 소스 품질 평가는 별도 게이트가 아니라 해체의 부산물로 드러낸다.
- 단일 소스 해체는 NotebookLM Studio 보고서 기능, 다량 소스 스캐닝은 채팅창이 현재 검증된 실행 채널이다.
- "판단 비용을 먼저 낮추는" 1단계 스캔/판별 → 2단계 심화 패턴이 영상·보고서에 공통으로 작동한다.

### [2026-05-30] 소스 수집 파이프라인 아키텍처 문서화

- 3축 분류 체계(구조적 정형성·인식적 주관성·지식 반감기)에 대한 비판적 검토와 4대 채널(말/글/영상/경험) 관찰을 거쳐 2층위 파이프라인 아키텍처를 확정했다.
- `meta/SOURCE_INGESTION_PIPELINE.md` 신규 생성: Layer 1 인식론적 태그(DIRECT/MEDIATED) + Layer 2 매체 라우팅(TEXTUAL/ACOUSTIC/MULTIMODAL) + ACOUSTIC 전처리 루틴 4단계 + MULTIMODAL TBD 명시.
- `meta/catalog.md`에 "아키텍처 문서" 섹션 신설하여 등록했다. 프롬프트 성능 추적 테이블과 분리해 구분했다.
- **미결 과제**: MULTIMODAL 채널에서 음성(ACOUSTIC)과 시각(TEXTUAL) 분리 처리 후 재합산하는 방법이 아직 설계되지 않았다. `RES-002-G` 계열이 실용적으로 운용 중이나 명시적 재합산 규칙은 부재하다.

### [2026-05-30] 파일명 체계 전환 — 해체(digest) 계열

- 기존 `RES-002-X` 계열의 채널 코드(A=논문, C=보고서, G=영상)가 직관적이지 않다는 판단 하에 새 파일명 체계를 도입했다.
- **체계**: `{도메인}_{단계}_{채널}_{세부유형}_{행위}` (예: `res_digest_text_report_scan`)
- **단계 구분**: `collect`(수집) / `digest`(해체) / `build`(자산화) — 해체 계열만 우선 전환, 수집·자산화는 추후 전환 예정.
- **rename 대상**: lab 2개, packages/core 5개, packages/adapters 7개, packages/builds 5개 — 총 19개 파일.
- 파일 내부 교차 참조(어댑터↔코어, 파이프라인 다음 단계 안내 등) 전수 교체 완료. 잔존 구 ID 0건 확인.
- `catalog.md`를 수집/해체/자산화 3개 섹션으로 재구성. 해체 테이블에 구 ID 대조 컬럼 추가.
- `eval/runs/` 파일명은 과거 실행 기록 보존을 위해 의도적으로 변경하지 않았다.
- 발견된 사전 불일치: adapters에 코어가 없는 고아 파일(`res_digest_video_route_legacy.notebooklm.md`)이 존재했음. legacy로 처리했다.

### [2026-05-31] 원칙/지침 층위 정립과 프롬프트 작성 지침 신설

- 문서 체계를 **원칙(가고자 하는 방향)**과 **지침(현재 지형에서 그 방향을 유지하는 방법)**의 두 층으로 명시 구분했다. 지형이 바뀌면 지침은 다시 쓰되 방향은 그대로다 — 그래서 라우팅·전처리 같은 운영 규칙은 원칙이 아니라 지침이다.
- 문서가 **두 트랙**으로 내려옴을 드러냈다. 지식 트랙(`KNOWLEDGE_SYSTEM`→`SOURCE_INGESTION_PIPELINE`)은 소스를 어떻게 다루는가, 프롬프트 트랙(`DESIGN_PRINCIPLES`→`PROMPT_DRAFTING_GUIDE` 작성 / `CORE_ADAPTER_ARCHITECTURE` 포장)은 아티팩트를 어떻게 만드는가를 맡는다. `SOURCE_INGESTION`은 "프롬프트 설계 지침"이 아니라 "소스 처리 지침"임을 분명히 했다.
- `meta/PROMPT_DRAFTING_GUIDE.md` 신설(골격). 원칙별 작성 규칙 5블록에 **정방향(어느 방향을 유지하나)·역방향(반복 실패 시 어느 원칙을 의심하나) 링크**를 달아, 지침이 원칙을 떠받치는 동시에 원칙 환류 트리거까지 가리키게 했다. 지난 "모든 것은 텍스트다" 최종안에서 드러난 방화벽 오류는 1-3에 "제약은 전역이 아니라 국면×태그 조건부" 규칙으로 박았다.
- `SOURCE_INGESTION_PIPELINE.md`에 "이 문서의 지위: `KNOWLEDGE_SYSTEM` 파생 지침" 헤더를 달고, 잔존 구 ID(3행 `RES-002 계열`→`해체(digest) 계열`)와 내부 호칭("해석 원칙"→"해석 기준")을 정리했다.
- 이전 rename에서 누락된 라이브 구 ID도 추가 정리: `library/research/index.md`, 영상 deep 어댑터, `eval/index.md`, route 코어의 "다음 단계" 파이프라인 안내(`RES-002-G-[모드]`→`res_digest_video_[모드]`, 빌드 재생성), `KNOWLEDGE_SYSTEM` 본문. 계보·이력 표기와 `eval/runs/` 파일명, catalog/resume의 구 ID 대조 컬럼은 의도적으로 보존.

### 다음 작업

- `res_digest_video_route`/`res_digest_video_deep` 영상 테스트를 `eval/runs/`에 정식 기록한다.
- 보고서 해체 파이프라인(`res_digest_text_report_scan`/`deep`)을 법정계획서와 정책보고서로 재검증한다.
- `PROMPT_DRAFTING_GUIDE.md` §1을 `lab/` 실험과 함께 실제 작성 규칙 문구로 채운다.
- `RES-000` 탐색 프롬프트와 `RES-003/004` 자산화 프롬프트의 실제 입력 테스트를 시작한다.
- `library/research/index.md`에는 `validated` 이상만 정식 승격시키고, 현재 후보는 후보로만 둔다.
