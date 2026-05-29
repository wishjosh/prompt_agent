#!/usr/bin/env python3
# NotebookLM 합본 빌드 스크립트 (Python 버전, build_notebooklm.ps1과 동일 동작)
# core/{base}.md + adapters/{base}.notebooklm.md  ->  notebooklm/{base}.notebooklm.md
#
# 합본은 코어+어댑터의 "파생물"이다. 직접 고치지 말고, core/ 또는 adapters/를 고친 뒤
# 이 스크립트를 재실행해 notebooklm/ 합본을 갱신하라. (drift 방지)
#
# 사용법:  python build_notebooklm.py
#         python build_notebooklm.py --root <경로> --out <출력경로>

import argparse
import re
from pathlib import Path


def clean_body(t: str) -> str:
    """작성용 메타 제거 — 실행에 필요한 본문만 남긴다."""
    t = re.sub(r"<!--.*?-->", "", t, flags=re.DOTALL)                 # HTML 주석
    lines = [ln for ln in re.split(r"\r?\n", t) if not re.match(r"^\s*>", ln)]  # '>' 안내/인용
    t = "\n".join(lines)
    t = re.sub(r"\[(필수|선택)\]\s*", "", t)                          # [필수]/[선택] 태그
    t = re.sub(r"^\|\s*(항목|ID|짝 코어|환경)\b.*$", "", t, flags=re.MULTILINE)  # 메타 헤더 표 행
    t = re.sub(r"^버전:.*$", "", t, flags=re.MULTILINE)              # 버전 푸터
    t = re.sub(r"^\s*$\n{2,}", "\n\n", t, flags=re.MULTILINE)        # 빈 줄 압축
    return t.strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="NotebookLM 합본 빌드")
    parser.add_argument("--root", default=str(Path(__file__).resolve().parent),
                        help="research 루트 경로 (기본: 스크립트 위치)")
    parser.add_argument("--out", default=None,
                        help="출력 경로 (기본: <root>/notebooklm)")
    args = parser.parse_args()

    root = Path(args.root)
    adapter_dir = root / "adapters"
    core_dir = root / "core"
    out_dir = Path(args.out) if args.out else root / "notebooklm"
    out_dir.mkdir(parents=True, exist_ok=True)

    count = 0
    for adapter_path in sorted(adapter_dir.glob("*.notebooklm.md")):
        base = adapter_path.name[: -len(".notebooklm.md")]
        core_path = core_dir / f"{base}.md"
        if not core_path.exists():
            print(f"skip (짝 코어 없음): {base}")
            continue

        core_text = clean_body(core_path.read_text(encoding="utf-8"))
        adp_text = clean_body(adapter_path.read_text(encoding="utf-8"))
        combined = f"{core_text}\n\n---\n\n{adp_text}\n"

        out_path = out_dir / f"{base}.notebooklm.md"
        out_path.write_text(combined, encoding="utf-8", newline="\n")  # BOM 없는 UTF-8, LF
        print(f"build: notebooklm/{base}.notebooklm.md  ({len(combined)} chars)")
        count += 1

    print(f"완료: {count} 개 합본 생성")


if __name__ == "__main__":
    main()
