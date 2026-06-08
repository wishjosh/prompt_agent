# NotebookLM Research Package

NotebookLM에서 반복 실행하기 위한 연구 프롬프트 패키지다.

## 구조

```text
research/
├── core/                 # 환경 중립 행위 정의
├── adapters/             # NotebookLM 실행 인터페이스
├── builds/               # core + adapter 합본
└── build_notebooklm.py   # 합본 생성 스크립트
```

## 빌드

```bash
python build_notebooklm.py
```

기본 출력 위치는 `builds/`다. 합본은 파생물이므로 직접 수정하지 않는다. 원본은 `core/`와 `adapters/`다.
