# NotebookLM 합본 빌드 스크립트
# core/{base}.md + adapters/{base}.notebooklm.md  ->  notebooklm/{base}.notebooklm.md
#
# 합본은 코어+어댑터의 "파생물"이다. 직접 고치지 말고, core/ 또는 adapters/를 고친 뒤
# 이 스크립트를 재실행해 notebooklm/ 합본을 갱신하라. (drift 방지)
#
# 사용법:  pwsh ./build_notebooklm.ps1   (또는 powershell -File build_notebooklm.ps1)

param([string]$Root = $PSScriptRoot)

$adapterDir = Join-Path $Root 'adapters'
$coreDir    = Join-Path $Root 'core'
$outDir     = Join-Path $Root 'notebooklm'
New-Item -ItemType Directory -Force $outDir | Out-Null

function Clean-Body([string]$t) {
    # 작성용 메타 제거 — 실행에 필요한 본문만 남긴다
    $t = [regex]::Replace($t, '(?s)<!--.*?-->', '')          # HTML 주석
    $lines = ($t -split "`r?`n") | Where-Object { $_ -notmatch '^\s*>' }  # '>' 안내/인용
    $t = ($lines -join "`n")
    $t = [regex]::Replace($t, '\[(필수|선택)\]\s*', '')       # [필수]/[선택] 태그
    $t = [regex]::Replace($t, '(?m)^\|\s*(항목|ID|짝 코어|환경)\b.*$', '')  # 메타 헤더 표 행(주요)
    $t = [regex]::Replace($t, '(?m)^버전:.*$', '')            # 버전 푸터
    $t = [regex]::Replace($t, "(?m)^\s*$\n{2,}", "`n`n")      # 빈 줄 압축
    return $t.Trim()
}

$count = 0
Get-ChildItem (Join-Path $adapterDir '*.notebooklm.md') | ForEach-Object {
    $base = $_.Name -replace '\.notebooklm\.md$', ''
    $corePath = Join-Path $coreDir "$base.md"
    if (-not (Test-Path $corePath)) {
        Write-Host "skip (짝 코어 없음): $base"
        return
    }
    $coreText = Clean-Body (Get-Content $corePath -Raw -Encoding UTF8)
    $adpText  = Clean-Body (Get-Content $_.FullName -Raw -Encoding UTF8)
    $combined = "$coreText`n`n---`n`n$adpText`n"
    $outPath  = Join-Path $outDir "$base.notebooklm.md"
    [System.IO.File]::WriteAllText($outPath, $combined, (New-Object System.Text.UTF8Encoding($false)))
    Write-Host ("build: notebooklm/{0}.notebooklm.md  ({1} chars)" -f $base, $combined.Length)
    $count++
}
Write-Host "완료: $count 개 합본 생성"
