# Prompt Agent

> 프롬프트의 재사용성보다 먼저, 실제 입력에서 원하는 사고와 출력을 끌어내는 성능을 검증한다.

## 목적

이 워크스페이스는 데이터, 정보, 지식 소스를 소화하고 체계적으로 정리하기 위한 프롬프트를 실험하고 선별하는 공간이다.

- 당장은 Claude, Gemini, NotebookLM, Claude Code, Antigravity 등에서 바로 실행 가능한 프롬프트를 만든다.
- 장기적으로는 하네스 엔지니어링 기반 에이전트의 자산으로 승격할 수 있는 프롬프트를 축적한다.
- 단, 에이전트 통합과 모듈화는 검증된 프롬프트에 적용하는 포장 단계다. 초안 단계의 중심은 성능 실험이다.

## 운영 원칙

1. **Test First**: 새 프롬프트는 먼저 실제 입력에 돌리고, 결과물로 판단한다.
2. **Prompt Before Module**: Atom, Composite, Core, Adapter는 초안의 출발점이 아니라 검증 후 정리 방식이다.
3. **Evidence Over Form**: 좋은 프롬프트인지의 근거는 메타데이터가 아니라 실행 결과, 실패 양상, 수정 이력이다.
4. **Promotion, Not Perfection**: 실험 프롬프트가 여러 입력에서 반복적으로 작동할 때만 `library/`나 `packages/`로 승격한다.

## 디렉터리 구조

```text
prompt_agent/
├── lab/                         # 프롬프트 실험실
│   ├── experiments/              # 아직 성능을 검증 중인 프롬프트
│   └── templates/                # 실험 기록 템플릿 + legacy 작성 템플릿
├── eval/                        # 성능 평가 계층
│   ├── scorecard.md              # 좋은 출력의 판단 기준
│   ├── index.md                  # 테스트 실행 기록 인덱스
│   └── runs/                     # 실제 실행 결과 보존
├── library/                     # 검증된 프롬프트의 사용 인덱스
├── packages/                    # 특정 실행 환경용 포장본
│   └── notebooklm/research/      # NotebookLM core/adapters/builds
├── legacy/                      # 전면 개편 전 자산과 경로 대응표
├── meta/                        # 원칙, 카탈로그, 아키텍처 참고 문서
└── journal/                     # 설계 논의와 개발 일지
```

## 작업 순서

1. `lab/experiments/`에서 단일 프롬프트를 만든다.
2. 실제 소스에 실행하고 결과를 `eval/runs/`에 남긴다.
3. `eval/scorecard.md` 기준으로 성공, 실패, 수정점을 기록한다.
4. 같은 목적의 다른 입력에서도 반복 테스트한다.
5. 성능이 확인되면 `library/`에 사용 대상으로 등록한다.
6. 특정 환경에서 반복 실행이 필요할 때만 `packages/`로 코어/어댑터를 포장한다.

## 승격 기준

- `draft`: 실행 가능한 초안
- `trialed`: 실제 입력 1회 이상 실행
- `revised`: 테스트 실패나 한계를 반영해 수정
- `validated`: 서로 다른 입력 3개 이상에서 핵심 기준 통과
- `stable`: 반복 사용 중인 표준 프롬프트
- `legacy`: 분리 전 원본 또는 참고용 보존본

현재 성능 현황은 [meta/catalog.md](meta/catalog.md)를 본다. 코어-어댑터 포장 규칙은 [meta/CORE_ADAPTER_ARCHITECTURE.md](meta/CORE_ADAPTER_ARCHITECTURE.md)를 보되, 초안 작성의 기본 절차로 사용하지 않는다. 전면 개편 전 자산은 [legacy/](legacy/)에서 확인한다.
