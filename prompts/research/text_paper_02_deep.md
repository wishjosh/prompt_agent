# text_paper_02_deep — 학술 문헌 2차 심층 해체

상태: draft
대상: 저널 논문 / 석·박사 학위논문 / 기타 학술 원고의 지정 장·절 또는 전체
주 실행 환경: NotebookLM Studio 보고서 작성
관련 프롬프트: text_paper_01_scan

## 사용 전 메모

- 논문 1편만 선택한다.
- `text_paper_01_scan`의 `2차 Deep 입력 블록`은 실행 코드블록 맨 아래 `DEEP INPUT BLOCK` 아래에 붙인다.
- NotebookLM Studio의 보고서 작성 프롬프트 제한에 맞춰 아래 코드블록만 복사한다.
- 실행 프롬프트는 영문 5,000자 미만이다.
- 붙여넣은 `DEEP INPUT BLOCK` 안의 target scope는 반드시 직접 채운다.

## 복사해서 실행할 프롬프트

```text
Deep-read ONE selected section/range of ONE journal article, master's thesis, doctoral dissertation, or other academic manuscript. Use compact bullets and tables.

Final answer: Korean headings, bullets, table labels, and handoff labels. Do not copy English labels. English allowed only for source titles, citations, tags, user terms.

Paste the first-scan Deep Input Block under DEEP INPUT BLOCK at the end. Output Section 0 must summarize and verify that input. If a full scan result is pasted instead, recover only the deep candidates, paper architecture, and scan-level gaps.

Goal: expose the author's structure, core argument, evidence, method, limits, and secondary clues without judging the paper.

Rules:
- Use only the selected source. No outside facts, theory summaries, or method critique.
- Analyze only target scope. If a scan gap/handoff item is outside it, mark outside target scope in Section 0 and do not analyze it in Sections 1-6.
- Preserve the author's original order. Do not reorganize into a smoother logic.
- Do not force IMRaD if the paper is not IMRaD.
- Recover the first-scan candidate reason and researcher focus.
- Cite every key item with NotebookLM marker plus page/section. If page is unclear, use section name.
- Use only these tags: [Fact], [Data], [Author Claim], [Method], [Limit], [Implication].
- Distinguish author-stated limits from scan-level gaps.
- Do not define concepts from general knowledge. If the source does not define a term, write a Korean equivalent of "no source definition - needs review."
- No quality judgment, including journal prestige or validity.
- Do not add final synthesis, advice, strategic insight, or recommendations beyond source-stated content.

Output structure. English names are schema only; translate headings into Korean. Do not output English section headings.

# [Korean of "Deep Dissection"]_[source title] - [target scope]

## 0. [Korean of "Scope Check"]
- Target scope: [target section/range]
- Handoff use: [used / recovered from full scan / none]
- First-scan candidate reason: [1-2 lines, or none]
- User note reflected: [focus/context/output request, or none]
- Scan gaps or handoff items: [relevant / outside target scope / none]

## 1. [Korean of "Structure X-ray in Source Order"]
State that the order is not reorganized.
- [source part] - function: [problem/literature/theory/method/data/analysis/result/discussion/limit/etc.] [citation+location]
- [source part] - function: [...] [citation+location]
- Development mechanism: [IMRaD / problem-theory-case-discussion / conceptual / historical / comparative / method proposal / other]

## 2. [Korean of "Concept, Theory, and Literature Position"]
| Item | Role in source | Definition/explanation | Location |
|---|---|---|---|
| [concept/theory/work] | [definition/frame/background/gap/support] | [source-stated content OR no source definition - needs review] | [citation+location] |

## 3. [Korean of "Method, Data, and Unit"]
- Method: [method/procedure] [citation+location]
- Data: [data/source/sample/case] [citation+location]
- Unit of analysis: [unit] [citation+location]
- Spatial/temporal scope: [scope] [citation+location]
- Variables/indicators/coding: [if any, or none] [citation+location]

## 4. [Korean of "Core Arguments"]
State that this follows the source order.
- [source part] - [Fact/Data/Author Claim/Method/Limit/Implication] [claim or finding] / evidence: [evidence] [citation+location]
- [source part] - [tag] [claim or finding] / evidence: [evidence] [citation+location]

## 5. [Korean of "Secondary Sparks"]
- Unusual method/approach: [item, or none] [citation+location]
- Passing limit/footnote: [item, or none] [citation+location]
- Exceptional data/phenomenon: [item, or none] [citation+location]
- Literature-tracking clue: [work/author and role in this paper only, or none] [citation+location]

## 6. [Korean of "Limits and Scan Gaps"]
- Author-stated limits: [author-stated limits, or not confirmed] [citation+location]
- Scan-level gaps: [not confirmed in scan/deep, no guessing, or none] [location]
- Items for researcher verification: [items, or none]

Self-check: headings Korean; no English section headings; target scope not expanded; out-of-scope items only in Section 0; no final synthesis/advice/insight; source-only; original order kept; no quality judgment; no general-knowledge definitions; tags added; limits/gaps separated; citations include page/section.

DEEP INPUT BLOCK:
[paste Section 5, Deep Input Block, from text_paper_01_scan here. Then fill target scope, analysis focus, research context, and output request inside the pasted block.]
```

## 검토·수정용 한글 버전

> 이 섹션은 사람이 읽고 수정하기 위한 한글 대응본입니다. NotebookLM에는 위의 순영문 코드블록만 복사합니다.

저널 논문, 석사학위논문, 박사학위논문, 기타 학술 원고 중 1편의 지정 장·절 또는 범위를 심층 해체한다. 학술대회 발표문, 프리프린트, 워킹페이퍼, 디스커션 페이퍼는 `기타 학술 원고`의 하위 형태로 본다. 출력은 한국어로 작성하고, 글머리표와 표를 간결하게 사용한다.

입력란 사용: 실행 코드블록 맨 아래 `DEEP INPUT BLOCK`에 1차 스캔 결과의 `5. 2차 Deep 입력 블록`을 그대로 붙인다. 붙인 블록 안의 심화 범위, 분석 초점, 연구 맥락, 출력 요청을 직접 채운다. 출력의 `0. 적용 확인`은 이 입력 블록을 회수해 요약하는 섹션이다.

최종 출력 언어 규칙: 모든 제목, 글머리표, 표 라벨, 인계 블록 라벨을 한국어로 작성한다. 이 프롬프트의 영어 라벨을 그대로 복사하지 않는다. 영어는 소스 제목, 인용 마커, 태그, 사용자가 제공한 용어에만 허용한다.

목표: 논문을 평가하지 않고 저자의 구조, 핵심 논증, 근거, 방법, 한계, 주변부 단서를 드러낸다.

규칙:
- 선택된 단일 소스만 사용한다. 외부 사실, 이론 요약, 방법론 비판을 넣지 않는다.
- 지정한 심화 범위만 분석한다. 1차 스캔 공백이나 인계 항목이 지정 범위 밖이면 `0. 적용 확인`에서만 범위 밖으로 표시하고 본문 분석에는 끌고 오지 않는다.
- 저자의 원래 순서를 보존한다. 더 매끄러운 논리로 재구성하지 않는다.
- 논문이 IMRaD 형식이 아니면 IMRaD를 강제하지 않는다.
- 1차 스캔의 후보 이유와 연구자 초점을 회수한다.
- 저널의 신뢰도·인지도·등재 여부를 평가하지 않는다. 피어리뷰나 색인 여부는 원문에 명시된 경우에만 기록한다.
- 핵심 항목에는 NotebookLM 인용 마커와 페이지·섹션 위치를 함께 붙인다.
- 페이지가 불명확하면 섹션명을 사용한다.
- `[Fact]`, `[Data]`, `[Author Claim]`, `[Method]`, `[Limit]`, `[Implication]`을 구분한다.
- 저자가 명시한 한계와 스캔상 공백을 구분한다.
- 개념은 일반 지식으로 정의하지 않는다. 원문 정의가 없으면 `본문 정의 없음 - 추가검토`로 표시한다.
- 논문 품질 평가를 하지 않는다.
- 원문에 없는 최종 종합, 조언, 전략적 통찰, 제언을 추가하지 않는다.
- 실행 프롬프트의 영어 구조명은 내부 스키마일 뿐이며, 실제 출력 제목은 한국어로 번역한다.

출력 구조:
- `2차 심층 해체_[소스 제목] - [심화 범위]`
- `0. 적용 확인`
- `1. 엑스레이 구조`
- `2. 개념·이론·문헌 위치`
- `3. 방법·자료·분석 단위`
- `4. 핵심 논증`
- `5. 주변부 특이점`
- `6. 한계와 스캔상 공백`

---

최종 수정: 2026-06-04 (NotebookLM용 순영문 5,000자 미만 실행 프롬프트 + 검토용 한글본)
