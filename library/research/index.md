# Research Prompt Library

> 아직 `stable`로 승격된 프롬프트는 없다. 아래는 `research_agent`가 후보 도구로 참조할 수 있는 안정화 후보와 다음 검증 항목이다.

## 사용 경계

- 이 문서는 실행 프롬프트 원본이 아니라 후보 도구 인덱스다.
- `research_agent`는 이 목록을 참조해 도구를 추천할 수 있지만, 최종 실행 여부는 연구자 승인에 따른다.
- `validated` 미만 도구는 기본 도구가 아니라 후보 도구다. 추천 시 현재 상태와 남은 검증 항목을 함께 알려야 한다.
- `draft` 상태 프롬프트는 이 목록에 올리지 않는다. 초안은 `lab/`과 `meta/catalog.md`에서만 관리한다.

## Candidates

| ID | 이름 | 실행 위치 | 현재 상태 | 안정화 전 필요한 것 |
|----|------|----------|----------|-------------------|
| res_digest_multi_scan | 다중 소스 스캐닝 | [lab](../../lab/experiments/research/RES/res_digest_multi_scan.md) | revised | 다른 주제의 대규모 소스에서 군집 누락 여부 재검증 |
| res_digest_text_report_scan | 방대 보고서 1차 스캔 | [package core](../../packages/notebooklm/research/core/res_digest_text_report_scan.md) | revised | 법정계획서와 정책보고서 입력 테스트 |
| res_digest_text_report_deep | 보고서 2차 심층 해체 | [package core](../../packages/notebooklm/research/core/res_digest_text_report_deep.md) | revised | scan 맥락 임베드 방식 재실행과 비교 |
| res_digest_video_route | 영상 모드 판별기 | [package core](../../packages/notebooklm/research/core/res_digest_video_route.md) | trialed | 영상 유형별 라우팅 테스트 기록 파일화 |
| res_digest_video_deep | 영상 단일 소스 심층 해체 | [package core](../../packages/notebooklm/research/core/res_digest_video_deep.md) | trialed | 다중 화자/짧은 고밀도 영상 테스트 |
