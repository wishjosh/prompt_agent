# 소스 분류 원칙

프롬프트는 먼저 소스의 매체와 성격을 확인한 뒤, 그에 맞는 스캔 또는 deep 프롬프트를 고른다.

## 매체

- `TEXTUAL`: 논문, 보고서, 계획서, 법령, 기사, 단행본, 메모.
- `ACOUSTIC`: 인터뷰, 구술, 강연 녹취록처럼 말의 흔적이 강한 텍스트.
- `MULTIMODAL`: 영상, 화면 시연, 다큐, 강연 영상.

## 글 중심 단일 소스

- 저널 논문·석박사 학위논문·기타 학술 원고: `prompts/research/text_paper_01_scan.md`
- 연구보고서·정책보고서·계획서 등 보고서 계열: `prompts/research/text_report_01_scan.md`

## 수집 전 설계

- 새 연구 주제의 소스 바구니·검색어·가정 점검: `prompts/research/collect_00_search_brief.md`

## 다중 소스 묶음

- 목적 수집 또는 무기록 축적 소스 묶음의 지형 파악: `prompts/research/multi_source_01_scan.md`

## 처리 원칙

- 새 주제는 실제 수집 전에 `collect_00_search_brief.md`로 검색 브리프를 먼저 만든다.
- 다중 소스 묶음은 먼저 `multi_source_01_scan.md`로 소스 회계와 군집 지도를 만든다.
- 보고서 계열 단일 소스는 1차 스캔에서 구조 X-ray와 Target scope 후보를 만든 뒤, 연구자가 후보를 유지·수정·추가하여 deep으로 넘긴다.
- 학술 계열 단일 소스는 먼저 scan으로 구조를 잡고, 필요한 범위만 deep으로 넘긴다.
- 영상·구술 소스는 현재 단순 구조의 우선 범위 밖이다. 기존 실험은 `archive/old_structure`에 보존한다.
