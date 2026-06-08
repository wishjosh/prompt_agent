# Migration Map

전면 개편 전 주요 경로와 현재 위치의 대응표다.

## Prompt Drafts

| 이전 경로 | 현재 위치 |
|----------|----------|
| `prompts/research/RES/` | `lab/experiments/research/RES/` |
| `prompts/personal/` | `lab/experiments/personal/prompts/` |
| `prompts/templates/` | `legacy/templates/` |

## NotebookLM Package

| 이전 경로 | 현재 위치 |
|----------|----------|
| `prompts/research/core/` | `packages/notebooklm/research/core/` |
| `prompts/research/adapters/` | `packages/notebooklm/research/adapters/` |
| `prompts/research/notebooklm/` | `packages/notebooklm/research/builds/` |
| `prompts/research/build_notebooklm.py` | `packages/notebooklm/research/build_notebooklm.py` |

## Evaluation

| 이전 경로 | 현재 위치 |
|----------|----------|
| `test_results/` | `eval/runs/` |

## Index Documents

| 문서 | 현재 역할 |
|------|----------|
| `README.md` | 전체 운영 원칙과 구조 |
| `meta/catalog.md` | 프롬프트 성능 현황판 |
| `eval/scorecard.md` | 실행 결과 평가 기준 |
| `library/research/index.md` | 안정화 후보 인덱스 |
| `meta/CORE_ADAPTER_ARCHITECTURE.md` | 검증 후 포장 규칙 |
