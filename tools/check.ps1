# Runs all local quality checks. Stops at the first failure.
$checks = @(
    @("pytest", "--cov"),
    @("ruff", "check", "."),
    @("ruff", "format", "--check", "."),
    @("mypy")
)

foreach ($check in $checks) {
    Write-Host "`n==> uv run $($check -join ' ')" -ForegroundColor Cyan
    uv run @check
    if ($LASTEXITCODE -ne 0) {
        Write-Host "FAILED: $($check -join ' ')" -ForegroundColor Red
        exit $LASTEXITCODE
    }
}

Write-Host "`nAll checks passed." -ForegroundColor Green
