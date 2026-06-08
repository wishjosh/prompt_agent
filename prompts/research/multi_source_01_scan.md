# multi_source_01_scan — 다중 소스 1차 스캔

상태: draft
대상: 목적을 가지고 수집했거나, 기록 없이 쌓인 다량의 논문·보고서·기사·자료 묶음
주 실행 환경: NotebookLM 일반 채팅창
관련 프롬프트: collect_00_search_brief, text_paper_01_scan, text_report_01_scan

## 사용 전 메모

- 스캔할 소스 묶음을 모두 선택한다.
- NotebookLM에서는 다중 소스 선택 후 일반 채팅창 실행을 우선한다. 보고서 계열 단일 소스도 `text_report_01_scan`을 일반 채팅창에서 진행한다.
- 아래 순영문 코드블록만 복사한다.
- 실행 프롬프트는 영문 5,000자 미만이다.
- 연구 주제, 수집 목적, 원하는 군집 기준이 있으면 코드블록 맨 아래 입력란에 짧게 덧붙인다.
- 소스가 100개 이상이면 1차 지형도 작성 후 큰 군집을 다시 나누는 후속 스캔이 필요할 수 있다.

## 복사해서 실행할 프롬프트

```text
Scan ALL currently selected sources in NotebookLM chat.

Final answer: Korean headings, bullets, and table labels. Do not copy English labels. English allowed only for source titles, citations, tags, user terms.

Goal: first-pass map of a source bundle, not deep summaries: accounting, types, topic/role clusters, peripheral sources, duplicates/low-info/out-of-scope, next actions.

Rules:
- Use only selected sources. Do not add outside sources or recommendations.
- Start with source accounting before cluster interpretation.
- Keep source type separate from source role. Type means format/origin; role means how it helps the research.
- Try to place every visible source in one bucket: main cluster, peripheral, duplicate/similar, low-info/out-of-scope, or unclear.
- Do not judge quality. You may note fit, density, and need for later scan/deep with evidence.
- Mark uncertain title/type/role/cluster decisions as tentative or needs check.
- If the source list is too large or not fully visible, state the limit and propose split-scan criteria.
- Cite representative sources and important classification claims with NotebookLM markers. If exact source identity is unclear, say so.
- Do not add an essay-style final synthesis outside the requested sections.

Output structure. English names are schema only; translate all headings into Korean.

# [Korean of "Multi-source Scan"]_[research topic or bundle name]

## 0. [Korean of "Run Conditions"]
- Research topic/bundle name: [...]
- Collection context: [purposeful collection / accumulated without notes / mixed / not confirmed]
- User clustering hint: [...]
- Applied clustering rule: [...]
- Processing limit: [source count, title visibility, citation limit, or none]

## 1. [Korean of "Source Accounting"]
| Status | Count | Note |
|---|---:|---|
| Included in main clusters | [N] | [...] |
| Preserved as peripheral | [N] | [...] |
| Duplicate/similar | [N] | [...] |
| Low-info/out-of-scope | [N] | [...] |
| Unclear | [N] | [...] |

## 2. [Korean of "Source Type Map"]
| Source type | Count | Role in this bundle | Representative sources | Needs check |
|---|---:|---|---|---|
| Journal articles | [N] | [...] | [2-3 sources+citation] | [...] |
| Degree theses/dissertations | [N] | [...] | [...] | [...] |
| Other academic manuscripts | [N] | [conference/preprint/working/discussion papers, etc.] | [...] | [...] |
| Public reports/plans | [N] | [...] | [...] | [...] |
| Private/NGO/international reports | [N] | [...] | [...] | [...] |
| Laws/statistics/data | [N] | [...] | [...] | [...] |
| News/opinion/media | [N] | [...] | [...] | [...] |
| Other/unclear | [N] | [...] | [...] | [...] |

## 3. [Korean of "Topic and Role Clusters"]

### [Korean of "Cluster"] A. [cluster name] ([N] sources)
- Role: [discourse / concept-theory / method-indicator / empirical case / policy-institution / stakeholder discourse / data-status]
- Shared question: [...]
- Shared storyline: [max 2 lines]
- Representative sources:
  - [title] - [one-line contribution] [citation]
  - [title] - [one-line contribution] [citation]
- Other member sources: [list titles if possible; if too many, say split scan needed]
- Next action: [single-source scan/deep / split cluster scan / hold / collect more]

### [Korean of "Cluster"] B. [cluster name] ([N] sources)
- Role:
- Shared question:
- Shared storyline:
- Representative sources:
- Other member sources:
- Next action:

## 4. [Korean of "Peripheral or Value-Reversal Candidates"]
- [title] - peripheral reason: [...] / why preserve: [method, case, discourse, data, etc.] [citation]

## 5. [Korean of "Duplicate, Low-info, or Out-of-scope"]
- Duplicate/similar: [titles] - action: [merge / choose representative / check original]
- Low-info/missing full text: [titles] - action: [get full text / keep abstract only / exclude candidate]
- Out-of-scope: [titles] - action: [archive for other topic / exclude candidate]

## 6. [Korean of "Next Processing Plan"]
- First single-source scan candidates:
  - [title] - reason: [theory/method/data/policy density]
- First deep candidates:
  - [title or cluster] - reason: [...]
- Clusters needing split scan:
  - [cluster] - split by: [method / region / period / source type / argument]
- Collection gaps:
  - [missing source type or topic]

## 7. [Korean of "Alternative Classification Rules"]
- Alternative rule 1: [by source type / method / region / period / policy phase / discourse position] - why useful: [...]
- Alternative rule 2: [...] - why useful: [...]

Self-check: headings Korean; no English section headings; accounting first; type and role separate; peripheral sources preserved; duplicates/low-info/out-of-scope not dropped; uncertain items marked; no outside sources; no final essay synthesis.

INPUTS:
RESEARCH_TOPIC:
COLLECTION_CONTEXT:
CLUSTERING_HINT:
PRIORITY_QUESTION:
SOURCE_COUNT_NOTE:
```

## 검토·수정용 한글 버전

> 이 섹션은 사람이 읽고 수정하기 위한 한글 대응본입니다. NotebookLM에는 위의 순영문 코드블록만 복사합니다.

NotebookLM 일반 채팅창에서 현재 선택된 모든 소스를 1차 스캔한다.

최종 출력 언어 규칙: 모든 제목, 글머리표, 표 라벨은 한국어로 작성한다. 이 프롬프트의 영어 라벨을 그대로 복사하지 않는다. 영어는 소스 제목, 인용 마커, 태그, 사용자가 제공한 용어에만 허용한다.

목표: 단일 소스 심층 요약이 아니라, 소스 묶음의 전체 지형을 만든다. 소스 회계, 소스 유형, 주제·역할 군집, 주변부 후보, 중복·저정보·범위 밖 항목, 후속 처리 계획을 산출한다.

규칙:
- 선택된 소스만 사용한다. 외부 소스를 새로 추천하거나 목록에 넣지 않는다.
- 군집 해석보다 소스 회계를 먼저 제시한다.
- 소스 유형과 소스 역할을 분리한다.
- 모든 보이는 소스는 가능한 한 주요 군집, 주변부, 중복·유사중복, 저정보·범위 밖, 분류 불명 중 하나에 배치한다.
- 소스 품질을 평가하지 않는다. 다만 연구 목적과의 적합성, 정보 밀도, 후속 scan/deep 필요성은 근거와 함께 표시한다.
- 제목·유형·역할·군집 판정이 불확실하면 추정 또는 확인 필요로 표시한다.
- 소스가 너무 많거나 전체 목록이 안정적으로 보이지 않으면 한계를 적고 후속 분할 스캔 기준을 제안한다.
- 대표 소스와 주요 분류 판단에는 NotebookLM 인용 마커를 붙인다.
- 지정된 섹션 밖에 에세이식 최종 종합을 덧붙이지 않는다.

출력 구조:
- `다중 소스 스캔_[연구 주제 또는 소스 묶음명]`
- `0. 실행 조건`
- `1. 소스 회계`
- `2. 소스 유형 지도`
- `3. 주제·역할 군집`
- `4. 주변부·가치 역전 후보`
- `5. 중복·저정보·범위 밖`
- `6. 후속 처리 계획`
- `7. 대안 분류 기준`

---

최종 수정: 2026-06-04 (NotebookLM 일반 채팅창용 순영문 5,000자 미만 실행 프롬프트 + 검토용 한글본)
