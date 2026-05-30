# Lab

`lab/`은 프롬프트를 잘 작동하게 만드는 실험 공간이다. 이 단계에서는 중복, 거친 표현, 환경 의존성이 있어도 괜찮다. 중요한 것은 실제 입력에서 원하는 출력이 나오는지다.

## 원칙

- 먼저 단일 프롬프트를 완성한다.
- 테스트 없이 Atom, Composite, Core, Adapter로 쪼개지 않는다.
- 프롬프트가 실패하면 실패 양상을 먼저 적고, 그다음 구조를 고친다.
- 같은 실패가 반복될 때만 공통 규칙이나 템플릿으로 추출한다.

## 구성

- `experiments/`: 실행 가능한 초안과 실험 중인 프롬프트
- `templates/experiment.md`: 새 실험을 시작할 때 쓰는 최소 템플릿
- `templates/run_record.md`: 실행 결과를 기록할 때 쓰는 템플릿
레거시 Atom/Composite/Adapter 템플릿은 [`../legacy/templates/`](../legacy/templates/)에 보존한다. 검증 후 포장 단계에서만 참고한다.
