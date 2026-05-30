# Legacy

> 전면 개편 전 자산을 숨기지 않고 찾을 수 있게 둔 보존 구역이다.

`legacy/`는 현재 운영의 중심이 아니다. 새 실험은 `lab/`, 성능 검증은 `eval/`, 환경별 실행본은 `packages/`를 쓴다. 다만 이전 구조와 템플릿을 추적할 필요가 있을 때 여기서 확인한다.

## 구성

- `templates/`: 기존 Atom/Composite/Adapter 템플릿과 deprecated 단일 템플릿
- `migration-map.md`: 전면 개편 전 경로와 현재 위치의 대응표

## 현재 기준

- 기존 프롬프트 초안은 `lab/experiments/`로 이동했다.
- NotebookLM용 코어/어댑터/합본은 `packages/notebooklm/research/`로 이동했다.
- 기존 테스트 결과는 `eval/runs/`로 이동했다.
- 레거시 템플릿은 참고용이다. 새 실험은 `lab/templates/experiment.md`를 우선한다.
