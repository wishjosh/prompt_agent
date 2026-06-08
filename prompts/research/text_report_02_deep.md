# text_report_02_deep — 보고서 2차 발췌독

상태: working draft
대상: 보고서 계열 소스의 선택 장·절
주 실행 환경: NotebookLM 일반 채팅창
관련 프롬프트: text_report_01_scan

## 사용 전 메모

- 보고서 1편만 선택한다.
- 1차 스캔 전체를 붙이지 않는다.
- `text_report_01_scan`의 `2. 심층 후보 및 연구자 선택 블록`에서 실제 분석할 `Target scope` 1개를 우선 골라 아래 `DEEP INPUT BLOCK`에 붙인다.
- 입력이 길면 `Target scope` 1개씩 나누어 실행한다.

## 복사해서 실행할 프롬프트

```text
선택된 보고서 1편에서 DEEP INPUT BLOCK에 적힌 Target scope만 발췌독한다.
1차 스캔 전체를 재분석하지 말고, 지정 범위 안의 원문 내용만 해체한다.

규칙:
- 선택 소스와 DEEP INPUT BLOCK만 사용한다. 외부 사실, 법률 조언, 정책 설계 금지.
- Scope 밖 내용은 본문 분석에 넣지 않는다. 확인 항목이 범위 밖이면 0번에만 `범위 밖`.
- 원문 순서를 보존한다. 더 매끄러운 논리로 재구성하지 않는다.
- 핵심 항목마다 위치와 NotebookLM 인용 마커를 함께 쓴다. 예: p.8 [SOURCE_IMAGE_23].
- 페이지 번호만 단독으로 쓰지 않는다. 인용 마커가 보이지 않으면 `위치 미확인`이라고 쓴다.
- `SOURCE_IMAGE_N`만 단독으로 쓰지 않고 줄여 쓰지도 않는다.
- 용어는 원문이 정의한 경우만 정의한다. 정의가 없으면 `본문 정의 없음 - 추가검토`.
- 핵심 항목에는 [Fact], [Data], [Author Claim], [Recommendation], [Limit], [Method] 중 하나 이상을 붙인다.
- 원문에 없는 평가, 수사, 최종 종합, 실행 권고를 넣지 않는다.

# 2차 발췌독_[소스 제목] - [Target scope]

## 0. 적용 확인
| 항목 | 내용 |
|---|---|
| 분석 범위 | [Target scope의 Scope] |
| 후보 이유 | [Selection reason] |
| 분석 초점 | [Additional analysis focus] |
| 출력 요청 | [Focus/output request, 또는 없음] |
| 범위 밖 확인 항목 | [있으면 범위 밖으로 표시, 없으면 없음] |

## 1. 원문 순서 발췌독
### [Target scope 번호 또는 이름]
- [원문 위치] - [태그] [핵심 사실·수치·주장·한계] [위치+인용]
- [원문 위치] - [태그] [내용] [위치+인용]

## 2. 데이터·용어·방법
| 항목 | 내용 | 위치 |
|---|---|---|
| 주요 데이터/수치 | [표·그림·수치, 또는 없음] | [위치+인용] |
| 용어 | [원문 정의 또는 본문 정의 없음 - 추가검토] | [위치+인용] |
| 방법/자료 출처 | [있으면 작성, 없으면 없음] | [위치+인용] |

## 3. 대안·시나리오·추적 대상
| 유형 | 내용 | 위치 |
|---|---|---|
| 대안/시나리오 | [원문이 제시한 경우만] | [위치+인용] |
| 원문상 한계 | [있으면 작성, 없으면 없음] | [위치+인용] |
| 추가 확인 필요 | [근거 부족, 수치 불명확, 범위 밖 질문 등] | [위치+인용 또는 없음] |

최종 점검: 지정 Scope만 분석, 발췌독 유지, 외부 사실 없음, 위치 먼저·인용 마지막.

DEEP INPUT BLOCK:
Source title:
Research context:
Target scope 1:
- Scope:
- Selection reason:
- Additional analysis focus:
- Focus/output request:
Verification items:
- Location issue:
- Method/number issue:
- Legal/institutional issue:
Cross-scope request:
```
