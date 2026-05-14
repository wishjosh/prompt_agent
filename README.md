# Prompt Agent

> 개별 목표 행위를 잘 수행하는 프롬프트 설계가 최우선이다.

## 프로젝트 목적

이 프로젝트는 **프롬프트를 제작하고, 그 설계 과정의 논의를 축적**하는 워크스페이스다.

- 하네스 엔지니어링 및 에이전트 시스템 구축이 최종 목표이지만, 여기서는 그 시스템의 세부 요소에 해당하는 **프롬프트**에 집중한다.
- 프롬프트는 당장 대화창(Claude, Gemini 등), Claude Code, Antigravity 등에서 활용한다.
- 에이전트 시스템 통합(스킬화 등)은 이 프로젝트 내부에서 완결성이 확보된 이후에 별도로 진행한다.

## 현재 범위

- **도메인**: 연구 영역 (향후 다른 영역으로 확장 가능)
- **활용 환경**: 대화 기반 생성형 AI, Claude Code, Antigravity
- **외부 연계**: 없음 (내부 완결성 우선)

## 디렉토리 구조

```
prompt_agent/
├── README.md                    # 이 파일
├── DESIGN_PRINCIPLES.md         # 프롬프트 설계 원칙
├── prompts/                     # 프롬프트 보관소
│   ├── _template.md             # 작성 템플릿
│   └── research/                # 연구 도메인 프롬프트
├── meta/                        # 카탈로그
│   └── catalog.md               # 전체 프롬프트 목록
└── journal/                     # 사고 일지
    └── DIALOGUE.md              # 프롬프트 설계 논의 축적
```

## 설계 원칙 (요약)

자세한 내용은 [DESIGN_PRINCIPLES.md](DESIGN_PRINCIPLES.md) 참조.

1. **판단 지원** — 연구자의 판단을 대신하지 않고, 판단의 비용을 낮춘다
2. **마찰의 유형학** — Mechanical Friction은 제거, Cognitive Friction은 보존·강화
3. **역할 전환** — Facilitator(조력자) / Critical Friend(비판자) 모드 구분
4. **구조 → 세렌디피티** — 명확한 구조가 우연한 발견의 조건을 만든다

## 프롬프트 작성 방법

1. `prompts/_template.md`를 복사하여 새 프롬프트 파일 생성
2. 목표 행위, 마찰 분류, AI 역할을 먼저 정의
3. 절차와 출력 형식을 설계
4. 대화창에서 테스트 후 반복 개선
5. `meta/catalog.md`에 등록
6. 설계 과정의 사고 변화는 `journal/DIALOGUE.md`에 기록
