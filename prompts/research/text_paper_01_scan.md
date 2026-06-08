# text_paper_01_scan — 학술 문헌 1차 스캔

상태: draft
대상: 저널 논문 / 석·박사 학위논문 / 기타 학술 원고
주 실행 환경: NotebookLM Studio 보고서 작성
관련 프롬프트: text_paper_02_deep

## 사용 전 메모

- 논문 1편만 선택한다. 여러 소스를 동시에 선택하면 구조가 섞인다.
- NotebookLM Studio의 보고서 작성 프롬프트 제한에 맞춰 아래 코드블록만 복사한다.
- 실행 프롬프트는 영문 5,000자 미만이다.
- 연구 맥락이나 특별 주목 지점은 코드블록 맨 아래 `RESEARCH CONTEXT` 또는 `FOCUS`에 짧게 덧붙인다.

## 복사해서 실행할 프롬프트

```text
Scan ONE selected journal article, master's thesis, doctoral dissertation, or other academic manuscript.

Final answer: Korean headings, bullets, and table labels. In Section 5 only, keep exact English field labels. English allowed for source titles, citations, tags, user terms.

Goal: first-pass map before deep reading: source card, structure, architecture, assets/gaps, deep candidates, handoff block.

Rules:
- Use only the selected source; no outside facts, guesses, theory summaries, or critique.
- Preserve the author's section order. Do not reorganize.
- Use IMRaD only if the source itself follows it.
- Do not judge quality, validity, journal prestige, or peer-review/indexing unless the source states it.
- Separate author-stated limitations from scan-level gaps.
- No rhetoric or extra commentary. No insight, assessment, final summary, or recommendations.
- Cite key items with NotebookLM marker plus page/section; if no page, use section.
- In the deep input block, separate first-scan content from researcher-to-fill fields. Do not fill researcher choices.

Output structure. English names are schema only; translate headings into Korean. Do not output English section headings.

# [Korean of "First Scan"]_[source title]

## 0. [Korean of "Source Card"]
- Document type: [journal article/master's thesis/doctoral dissertation/degree thesis level unclear/other academic manuscript/etc.] [citation+location]
- Author / venue or publisher / year: [author] / [journal, university, or org] / [year] [citation+location]
- Field/topic: [field/topic] [citation+location]
- Research object: [object] [citation+location]
- Spatial scope / temporal scope: [space] / [time or data year] [citation+location]
- Data/method type: [method type] [citation+location]

## 1. [Korean of "Structure X-ray"]
Note that this preserves the author's order.
- [section/chapter] - function: [problem/literature/theory/method/data/analysis/results/discussion/limits/etc.] [location]
  - [subsection] - [main object or question] [location]
- [section/chapter] - function: [...] [location]
- Development mechanism: [IMRaD / conceptual / historical / comparative / other]

## 2. [Korean of "Paper Architecture"]
- Background/problem: [source-stated background/problem] [citation+location]
- Objective/RQ/hypothesis: [stated objective/RQ/hypothesis, or not confirmed] [citation+location]
- Theory/literature position: [theory, literature position, research gap as stated] [citation+location]
- Method/data/scope: [method, data, unit, scope] [citation+location]
- Core findings: [findings, key numbers/patterns] [citation+location]
- Conclusion/implication: [stated conclusion, implication, suggestion] [citation+location]
- Stated limits/future work: [author-stated limits/future work, or not confirmed] [citation+location]

## 3. [Korean of "Reusable Assets and Scan Gaps"]
- Concept assets: [definitions, distinctions, theory frame] [citation+location]
- Method assets: [design, variables, indicators, procedure, tools] [citation+location]
- Data assets: [sources, tables/figures, cases, survey/interview/stats] [citation+location]
- Literature-tracking candidates: [central cited works/authors and their role here only] [citation+location]
- Scan gaps: [method/date/RQ/data gaps not confirmed; no guessing] [location]

## 4. [Korean of "Deep Candidates"]
State that final choice belongs to the researcher.
- [chapter/section] - reason: [one-line reason: theory/method/data/result/limit density] [location]
- [chapter/section] - reason: [...] [location]
- [chapter/section] - reason: [...] [location]

## 5. [Korean of "Deep Input Block"]
Explain that the whole block below should be pasted into the DEEP INPUT BLOCK area of text_paper_02_deep, then filled by the researcher.

### 5-A. First-scan content
- Source title: [source title]
- Deep candidate 1: [chapter/section] - location: [page/section] - reason: [one line]
- Deep candidate 2: [chapter/section] - location: [page/section] - reason: [one line]
- Deep candidate 3: [chapter/section] - location: [page/section] - reason: [one line]
- Other selectable range: any other chapter/section from the Structure X-ray.
- Paper architecture core:
  - Objective/RQ: [...]
  - Theory/literature position: [...]
  - Method/data/scope: [...]
  - Core findings/conclusion: [...]
- Scan gaps: [...]

### 5-B. Researcher-to-fill fields
- Target scope: (leave blank)
- Additional analysis focus: (leave blank; e.g., concept, theory, variables, method, limits)
- Research context: (optional)
- Focus/output request: (optional; e.g., concept table, method reconstruction, literature tracking)

Self-check: headings Korean; no English section headings; Section 5 labels English; no insight/assessment/summary; source order kept; citations have page/section; handoff parts separate.

RESEARCH CONTEXT (optional):
FOCUS (optional):
```

## 검토·수정용 한글 버전

> 이 섹션은 사람이 읽고 수정하기 위한 한글 대응본입니다. NotebookLM에는 위의 순영문 코드블록만 복사합니다.

저널 논문, 석사학위논문, 박사학위논문, 기타 학술 원고 중 1편만 스캔한다. 학술대회 발표문, 프리프린트, 워킹페이퍼, 디스커션 페이퍼는 `기타 학술 원고`의 하위 형태로 본다.

최종 출력 언어 규칙: 일반 본문의 제목, 글머리표, 표 라벨은 한국어로 작성한다. 단, `5. 2차 Deep 입력 블록` 안의 필드 라벨은 2차 심층 프롬프트에 그대로 붙일 수 있도록 영어 라벨을 유지한다. 영어는 소스 제목, 인용 마커, 태그, 사용자가 제공한 용어에도 허용한다.

목표: 심층 정독 전 1차 구조 지도를 만든다. 소스 카드, 구조 X-ray, 논문 아키텍처, 재사용 가능한 자산과 공백, 심화 후보, 다음 프롬프트용 인계 블록을 산출한다.

규칙:
- 선택된 단일 소스만 사용한다. 외부 사실, 추정, 이론 요약, 방법론 비판을 넣지 않는다.
- 저자의 원래 섹션 순서를 보존한다. 재구성하지 않는다.
- 논문이 IMRaD 형식을 따를 때만 IMRaD 렌즈를 사용한다.
- 논문 품질이나 타당성을 평가하지 않는다.
- 저널의 신뢰도·인지도·등재 여부를 평가하지 않는다. 피어리뷰나 색인 여부는 원문에 명시된 경우에만 기록한다.
- 원문에 없는 평가성 수사, 통찰, 종합평, 제언을 추가하지 않는다.
- 저자가 명시한 한계와 스캔 단계에서 확인되지 않은 공백을 구분한다.
- 핵심 항목에는 NotebookLM 인용 마커와 페이지·섹션 위치를 함께 붙인다.
- 페이지가 불명확하면 섹션명을 사용한다.
- 2차 Deep 입력 블록은 1차 스캔 자동 내용과 연구자 작성 필드를 분리한다. 연구자의 선택을 대신 채우지 않는다.
- 2차 Deep 입력 블록은 2차 심층 프롬프트의 `DEEP INPUT BLOCK` 아래에 그대로 붙이는 입력 재료다.
- 실행 프롬프트의 영어 구조명은 내부 스키마일 뿐이며, 실제 출력 제목은 한국어로 번역한다.

출력 구조:
- `1차 스캔_[소스 제목]`
- `0. 소스 카드`
- `1. 구조 X-ray`
- `2. 논문 아키텍처 압축`
- `3. 재사용 가능한 자산과 스캔상 공백`
- `4. 심화 대상 후보`
- `5. 2차 Deep 입력 블록`
  - `5-A. 1차 스캔 내용`
  - `5-B. 연구자 작성 필드`

---

최종 수정: 2026-06-04 (NotebookLM용 순영문 5,000자 미만 실행 프롬프트 + 검토용 한글본)
