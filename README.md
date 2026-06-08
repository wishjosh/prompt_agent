# Prompt Agent

프롬프트를 만들고, 수동으로 실행하고, 실패를 기록하면서 고치는 작업대다.

지금은 검증된 프롬프트 패키지를 운영하는 단계가 아니다. 그래서 구조를 단순하게 유지한다.

## 구조

```text
prompt_agent/
├── principles/   # 원칙과 소스 분류
├── guides/       # 작성·실행 가이드
├── prompts/      # 실제로 복사해 쓰는 프롬프트
├── tests/        # 실행 기록과 평가 기준
└── archive/      # 예전 구조와 실험 보존
```

## 상위 토대

Josh의 철학적 사유 원문은 `prompt_agent` 내부가 아니라 [`../philosophy/josh_philosophical_thinking.md`](../philosophy/josh_philosophical_thinking.md)에 둔다. `prompt_agent`의 원칙은 이 문서를 바로 요약하지 않고, 충분히 검토되어 운영 기준으로 확정된 내용만 반영한다.

## 사용 순서

1. `prompts/`에서 프롬프트를 고른다.
2. 프롬프트 파일 안의 `사용 전 메모`를 확인한다.
3. `복사해서 실행할 프롬프트` 아래 본문을 NotebookLM 등 실행 환경에 붙여넣는다.
4. 결과를 `tests/runs/`에 남긴다.
5. 반복되는 실패를 프롬프트 파일에 반영한다.

## 현재 연구 프롬프트

- `prompts/research/collect_00_search_brief.md`
- `prompts/research/multi_source_01_scan.md`
- `prompts/research/text_paper_01_scan.md`
- `prompts/research/text_paper_02_deep.md`
- `prompts/research/text_report_01_scan.md`
- `prompts/research/text_report_02_deep.md`

## 보류한 것

`core`, `adapter`, `build`, `library`, `package` 구조는 당장 쓰지 않는다. 자동화가 필요해질 때 다시 꺼낸다. 기존 파일은 `archive/old_structure`에 보존한다.
