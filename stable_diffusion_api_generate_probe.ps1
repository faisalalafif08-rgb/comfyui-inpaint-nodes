$ErrorActionPreference = "Stop"

$outDir = "D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\03_shared_models_and_outputs\stable_diffusion_api_probe"
New-Item -ItemType Directory -Force -Path $outDir | Out-Null

$payload = @{
    prompt = "a realistic red apple on a wooden table, studio lighting, sharp focus"
    negative_prompt = "blurry, low quality, distorted"
    steps = 1
    sampler_name = "Euler"
    width = 256
    height = 256
    cfg_scale = 4
    seed = 12345
    batch_size = 1
    n_iter = 1
    send_images = $false
    save_images = $true
} | ConvertTo-Json -Depth 10

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$response = Invoke-RestMethod -Uri "http://127.0.0.1:7870/sdapi/v1/txt2img" -Method Post -Body $payload -ContentType "application/json" -TimeoutSec 1200

$appOutputs = "D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\02_stable_diffusion_webui\stable-diffusion-webui-master\stable-diffusion-webui-master\outputs"
$latestImage = Get-ChildItem -LiteralPath $appOutputs -Recurse -File -Include *.png,*.jpg,*.jpeg -ErrorAction SilentlyContinue |
    Sort-Object LastWriteTime -Descending |
    Select-Object -First 1

if ($null -eq $latestImage) {
    throw "API returned, but no saved output image was found under $appOutputs"
}

$imagePath = Join-Path $outDir "sdwebui_api_probe_$timestamp$($latestImage.Extension)"
Copy-Item -LiteralPath $latestImage.FullName -Destination $imagePath -Force

$report = [ordered]@{
    mode = "stable_diffusion_webui_api_probe"
    endpoint = "http://127.0.0.1:7870/sdapi/v1/txt2img"
    image_path = $imagePath
    source_image_path = $latestImage.FullName
    prompt = "a realistic red apple on a wooden table, studio lighting, sharp focus"
    width = 256
    height = 256
    steps = 1
    send_images = $false
    save_images = $true
    sampler_name = "Euler"
    seed = 12345
    created_at = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
}

$reportPath = Join-Path $outDir "sdwebui_api_probe_$timestamp.json"
$report | ConvertTo-Json -Depth 10 | Set-Content -Encoding UTF8 -LiteralPath $reportPath

Write-Host "DONE: Stable Diffusion API image generated"
Write-Host "Image: $imagePath"
Write-Host "Report: $reportPath"
