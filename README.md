# Prompt Agent

> 개별 목표 행위를 잘 수행하는 프롬프트 설계가 최우선이다.

## 프로젝트 목적

이 프로젝트는 **프롬프트를 제작하고, 그 설계 과정의 논의를 축적**하는 워크스페이스다.

- 하네스 엔지니어링 및 에이전트 시스템 구축이 최종 목표이지만, 여기서는 그 시스템의 세부 요소에 해당하는 **프롬프트**에 집중한다.
- 프롬프트는 당장 대화창(Claude, Gemini 등), Claude Code, Antigravity 등에서 활용한다.
- 에이전트 시스템 통합(스킬화 등)은 이 프로젝트 내부에서 완결성이 확보된 이후에 별도로 진행한다.

## 현재 범위

- **도메인**: 연구 영역 (Research), 개인/실험 영역 (Personal)
- **활용 환경**: 대화 기반 생성형 AI, Claude Code, Antigravity
- **외부 연계**: 없음 (내부 완결성 우선)

## 디렉토리 구조

```
prompt_agent/
├── README.md                    # 이 파일
├── prompts/                     # 프롬프트 보관소
│   ├── templates/               # 작성 템플릿 모음
│   │   ├── composite.md         # Composite 작성 템플릿 (한 호흡 완결 단위)
│   │   ├── atom.md              # Atom 작성 템플릿 (재사용 최소 단위)
│   │   ├── adapter.md           # Adapter 작성 템플릿 (환경별 실행본)
│   │   └── deprecated.md        # (deprecated) 구 단일 템플릿 — 참고용 보존
│   ├── research/                # 연구 도메인 (환경 중립 코어)
│   │   └── adapters/            # 환경별 어댑터 (NotebookLM 등)
│   └── personal/                # 개인/실험용 프롬프트
├── meta/                        # 시스템 설정 및 카탈로그
│   ├── DESIGN_PRINCIPLES.md     # 프롬프트 설계 원칙
│   ├── KNOWLEDGE_SYSTEM.md      # 지식 추출 및 정리 시스템 원칙
│   ├── CORE_ADAPTER_ARCHITECTURE.md  # 코어-어댑터 파일 구조 기준
│   └── catalog.md               # 전체 프롬프트 목록
└── journal/                     # 사고 일지
    ├── DIALOGUE.md              # 프롬프트 설계 논의 축적
    └── DEVELOPMENT.md           # 개발 일지
```

## 설계 원칙 (요약)

자세한 내용은 [DESIGN_PRINCIPLES.md](meta/DESIGN_PRINCIPLES.md) 참조.

1. **판단 지원** — 연구자의 판단을 대신하지 않고, 판단의 비용을 낮춘다
2. **마찰과 우선순위** — 어떤 마찰을 위임할지의 주도권은 연구자에게 있다
3. **역할 전환** — Facilitator(조력자) / Critical Friend(비판자) 모드 구분
4. **구조 → 세렌디피티** — 명확한 구조가 우연한 발견의 조건을 만든다

## 프롬프트 작성 방법

프롬프트는 환경 중립 **코어**와 환경별 **어댑터**로 나뉜다. 자세한 구조는 [CORE_ADAPTER_ARCHITECTURE.md](meta/CORE_ADAPTER_ARCHITECTURE.md) 참조.

1. 만들 단위에 맞는 템플릿을 복사:
   - 재사용 최소 단위 → `prompts/templates/atom.md`
   - 한 호흡 완결 단위 → `prompts/templates/composite.md`
   - 기존 코어의 환경별 실행본 → `prompts/templates/adapter.md`
2. **먼저 물어라**: 이 프롬프트가 연구자의 어떤 판단의 비용을 낮추는가? (필수 4섹션: 메타·목표·역할·제약)
3. 선택 섹션(절차·출력·위임·입력)은 필요한 것만 채우고, 불필요하면 섹션째 삭제한다.
4. 환경 의존 요소(소스 선택 방식·인용 마커 형식 등)는 코어에 넣지 말고 **어댑터로 분리**한다.
5. 여러 AI(NotebookLM·Claude·Codex 등)에서 테스트 후 반복 개선한다.
6. `meta/catalog.md`에 등록한다.
7. 설계 과정의 사고 변화는 `journal/DIALOGUE.md`에 기록한다.
