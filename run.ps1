$interpreter = "C:\Python311\python.exe"
$scriptPath = "main.py"

$command = "$interpreter $scriptPath"

Write-Host "Running script $scriptPath"
Write-Host "--------------------------"
Invoke-Expression -Command $command
Write-Host "--------------------------"
Write-Host "$scriptPath closed"