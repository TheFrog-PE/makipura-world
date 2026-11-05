$ErrorActionPreference = "Continue"

while ($true) {
    Write-Output "Iniciando túnel hacia localhost.run..."
    
    $processInfo = New-Object System.Diagnostics.ProcessStartInfo
    $processInfo.FileName = "ssh"
    $processInfo.Arguments = "-R 80:localhost:8080 -o StrictHostKeyChecking=no -o ServerAliveInterval=15 nokey@localhost.run"
    $processInfo.RedirectStandardOutput = $true
    $processInfo.RedirectStandardError = $true
    $processInfo.UseShellExecute = $false
    $processInfo.CreateNoWindow = $true

    $process = New-Object System.Diagnostics.Process
    $process.StartInfo = $processInfo
    $process.Start() | Out-Null

    while (-not $process.HasExited) {
        $line = $process.StandardOutput.ReadLine()
        if ($line) {
            Write-Output $line
            if ($line -match "https://[a-zA-Z0-9]+\.lhr\.life") {
                $url = $matches[0]
                Set-Content -Path "CURRENT_PUBLIC_URL.txt" -Value $url -Encoding UTF8
                Write-Output ">>> URL ACTIVA GUARDADA: $url <<<"
            }
        }
    }

    Write-Output "El túnel se desconectó. Reintentando en 3 segundos..."
    Start-Sleep -Seconds 3
}
