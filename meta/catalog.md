# 프롬프트 카탈로그

> 이 프로젝트에서 관리하는 모든 프롬프트의 목록.
> 프롬프트를 새로 작성하거나 상태가 변경될 때마다 이 테이블을 업데이트한다.

## 연구 도메인

| ID | 프롬프트명 | 목표 행위 | 위임 범위 | AI 역할 | 상태 | 버전 |
|----|-----------|----------|----------|--------|------|------|
| RES-000-A | [모드별 타겟팅 필터](../prompts/research/mode_specific_filter.md) | 수집된 소스를 특정 모드에 맞게 선별 | 소스 특성 분석 및 노이즈 제거 | F | draft | v1.1 |
| RES-000-B | [교차 모드 간극 분석](../prompts/research/cross_mode_gap_analysis.md) | 2개 이상 모드 간의 충돌 및 사각지대 도출 | 대조 분석 및 연구 질문 제안 | CF | draft | v1.1 |
| RES-000-C1 | [사회 인식 탐색 전략](../prompts/research/social_perception_exploration.md) | 대중 트렌드 및 편견 발굴 | 대중적 키워드 번역 및 커뮤니티 출처 추천 | F | draft | v1.1 |
| RES-000-C2 | [학술 이론 탐색 전략](../prompts/research/academic_theory_exploration.md) | 학술적 렌즈 및 거장 발굴 | 전문 용어 번역 및 핵심 이론 모형 제안 | F | draft | v1.1 |
| RES-000-C3 | [정책 현실 탐색 전략](../prompts/research/policy_reality_exploration.md) | 관련 법령 및 이해관계자 발굴 | 행정 용어 번역 및 정부/이익단체 출처 추천 | F | draft | v1.1 |
| RES-001 | [다중 소스 스캐닝](../prompts/research/multi_source_scanning.md) | 다량 문헌의 지형도 파악 | 1차 분류 및 군집화 (선택은 연구자) | F | draft | v1.1 |
| RES-002 | [단일 소스 심층 해체](../prompts/research/single_source_deep_dive.md) | 단일 문헌의 뼈대와 주변부 분리 추출 | 투명한 구조화 및 누락 방지 요약 | F | draft | v1.1 |
| RES-003 | [논리적 결합](../prompts/research/logic_fitting.md) | 인용 논리의 정합성 팩트체크 | 체리피킹 및 논리적 비약 검열 | CF | draft | v1.1 |
| RES-004 | [창조적 스파크](../prompts/research/action_fitting.md) | 파생 아이디어를 연구 씨앗으로 자산화 | 아이디어 구조화 및 Missing Links 경고 | CF | draft | v1.1 |

## 개인 도메인

| ID | 프롬프트명 | 목표 행위 | 위임 범위 | AI 역할 | 상태 | 버전 |
|----|-----------|----------|----------|--------|------|------|
| PER-001 | [사주 행동 분석](../prompts/personal/BaZi%20Behavioral%20Analysis.md) | 사주를 행동 분석의 거울로 활용하여 심리적 약점 및 성향 진단 | 행동 패턴 및 심리 분석 (운명 판단 배제) | CF | draft | v1.0 |

---

## 범례

**위임 범위**: 프롬프트가 다룰 수 있는 작업의 성격을 간략히 기술.
- Mechanical/Cognitive 분류는 참고 어휘로 사용하되, 고정 판정이 아닌 스펙트럼으로 취급한다.
- 같은 프롬프트라도 연구자의 상황과 우선순위에 따라 위임 여부가 달라진다.

**AI 역할**:
- `F` — Facilitator (조력자)
- `CF` — Critical Friend (비판자)
- `전환` — 국면별 역할 전환

**상태**:
- `draft` — 초안 작성 완료
- `tested` — 대화창에서 테스트 완료
- `production` — 실무 활용 중
- `deprecated` — 폐기 (사유 기재)

