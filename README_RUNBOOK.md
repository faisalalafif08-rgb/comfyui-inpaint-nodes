# Organized Generation Workspace - 2026-06-12

Root:
D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612

## What each package does

1. Fooocus-main(2).zip -> 01_fooocus/Fooocus-main_canonical
   - This is the clean Fooocus source. It has entry_with_update.py, launch.py, webui.py, models/, presets/, modules/.
   - Use this as the main Fooocus runtime.

2. Fooocus-release.zip -> 01_fooocus/Fooocus-release_minimal
   - Minimal Fooocus release layout.
   - Good as a small fallback/reference, but still needs model checkpoints.

3. Fooocus_Female_System_Windows.zip -> 01_fooocus/female_prompt_pack
   - Prompt pack only. It does not generate by itself.
   - Use PROMPTS_AR.txt or PROMPTS_EN.txt inside Fooocus prompt box.
   - Use NEGATIVE_PROMPT.txt in Negative Prompt.

4. Fooocus-main.zip and Fooocus-main(1).zip -> archive only
   - Same SHA256. They include __MACOSX metadata and a less clean layout.
   - Kept in 00_archives_original, not used as main runtime.

5. stable-diffusion-webui-master.zip -> 02_stable_diffusion_webui/stable-diffusion-webui-master
   - AUTOMATIC1111 WebUI source.
   - Use run_stable_diffusion_webui.bat after placing a checkpoint in models/Stable-diffusion.

## Run commands

Fooocus main:
04_run_scripts\run_fooocus_main_canonical.bat

Fooocus release:
04_run_scripts\run_fooocus_release_minimal.bat

Stable Diffusion WebUI:
04_run_scripts\run_stable_diffusion_webui.bat

## Model placement

Fooocus checkpoint models:
01_fooocus\Fooocus-main_canonical\Fooocus-main\models\checkpoints

Fooocus LoRA:
01_fooocus\Fooocus-main_canonical\Fooocus-main\models\loras

Stable Diffusion checkpoints:
02_stable_diffusion_webui\stable-diffusion-webui-master\stable-diffusion-webui-master\models\Stable-diffusion

Shared holding area:
03_shared_models_and_outputs

## Production rule

- Originals in C:\Amal.X were not modified.
- ZIPs were copied to 00_archives_original.
- Extracted working copies are under this workspace.
- No real image generation can complete until a valid model checkpoint exists in the required model folder or the app downloads one during startup.
