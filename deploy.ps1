Write-Host "Attempting to push your local profile README to your GitHub account..."
git push -u origin main
if ($LASTEXITCODE -eq 0) {
    Write-Host "Push successful. Your GitHub profile has been updated."
} else {
    Write-Host "Error: Push failed."
    Write-Host "Please ensure you have completed the following steps:"
    Write-Host "1. Go to https://github.com/new"
    Write-Host "2. Create a public repository named: naagasumukh8"
    Write-Host "3. Do not check 'Add a README file' (leave it empty)."
    Write-Host "4. Run this script again."
}
