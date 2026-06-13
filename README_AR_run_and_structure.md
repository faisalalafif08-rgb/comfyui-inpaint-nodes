# تشغيل وتنظيم حزم الإنتاج

المجلد المنظم:

```text
D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612
```

## التقسيم المعتمد

```text
00_archives_original
= نسخ ZIP الأصلية كما هي.

01_fooocus
= Fooocus الرئيسي + Fooocus release + حزمة Female prompts + entry_with_update_full.

02_stable_diffusion_webui
= AUTOMATIC1111 Stable Diffusion WebUI.

03_shared_models_and_outputs
= مخرجات الاختبار والإنتاج المشتركة.

04_run_scripts
= أوامر التشغيل الجاهزة.

05_docs_reports
= اللوقات والتقارير.

07_alzaeem_windows_ready
= نظام ALZaeem Windows Ready.

08_avatarforge
= AvatarForge profiles/docs.
```

## Fooocus الرئيسي

تشغيل:

```text
D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\04_run_scripts\run_fooocus_main_canonical.bat
```

الرابط:

```text
http://127.0.0.1:7869
```

إثبات الإنتاج:

```text
D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\01_fooocus\Fooocus-main_canonical\Fooocus-main\outputs\2026-06-12\2026-06-12_12-44-19_8093.png
```

## Fooocus entry_with_update الكامل

هذه نسخة Fooocus كاملة من:

```text
C:\Projects\5858\entry_with_update.zip
```

مكانها:

```text
D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\01_fooocus\entry_with_update_full
```

تشغيل بدون تحديث تلقائي:

```text
D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\04_run_scripts\run_fooocus_entry_with_update_full_no_update.bat
```

الرابط:

```text
http://127.0.0.1:7871
```

تم فحص التشغيل:

```text
http://127.0.0.1:7871/config
HTTP 200
```

## Stable Diffusion WebUI

تشغيل API مباشر:

```powershell
powershell -ExecutionPolicy Bypass -File "D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\04_run_scripts\run_stable_diffusion_webui_api_direct.ps1"
```

الرابط:

```text
http://127.0.0.1:7870
```

API model check:

```text
http://127.0.0.1:7870/sdapi/v1/sd-models
```

الحالة الحالية:

```text
API: يعمل
HTTP: 200
Model: juggernautXL_v8Rundiffusion.safetensors
SHA256: aeb7e9e6897a1e58b10494bd989d001e3d4bc9b634633cd7b559838f612c2867
```

إثبات الإنتاج من API:

```text
D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\03_shared_models_and_outputs\stable_diffusion_api_probe\sdwebui_api_probe_14471226_180013.png
```

ملاحظة: أول اختبار إنتاج كان سريع جدًا 1 step بحجم 256x256 لإثبات أن pipeline ينتج ملف صورة. جودة الصورة ليست معيار الاختبار هنا.

## ALZaeem Windows Ready

المصدر:

```text
C:\Projects\5858\ALZaeem_Windows_Ready.zip
```

المكان:

```text
D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\07_alzaeem_windows_ready\ALZaeem_Windows_Ready
```

تشغيل:

```text
D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\04_run_scripts\run_alzaeem_windows_ready.bat
```

## AvatarForge

المصادر:

```text
C:\Projects\5858\AvatarForge_Expanded_WithProfiles_And_Docs.zip
C:\Projects\5858\AvatarForge_Expanded_WithProfiles_And_Docs_v2.zip
```

المكان:

```text
D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\08_avatarforge
```

فتح نسخة v2:

```text
D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\04_run_scripts\open_avatarforge_v2_folder.bat
```

## سكربتات التشغيل

```text
04_run_scripts\run_fooocus_main_canonical.bat
04_run_scripts\run_fooocus_release_minimal.bat
04_run_scripts\run_fooocus_entry_with_update_full_no_update.bat
04_run_scripts\run_stable_diffusion_webui.bat
04_run_scripts\run_stable_diffusion_webui_api_no_pause.bat
04_run_scripts\run_stable_diffusion_webui_api_direct.ps1
04_run_scripts\run_stable_diffusion_webui_smoke_exit.bat
04_run_scripts\run_alzaeem_windows_ready.bat
04_run_scripts\open_avatarforge_v2_folder.bat
```

## القرار

```text
Fooocus main: منظم ويعمل وينتج.
Fooocus entry_with_update_full: منظم ويعمل على 7871 بدون تحديث تلقائي.
Stable Diffusion WebUI: منظم، API يعمل، وينتج ملف صورة اختبار.
ALZaeem Windows Ready: منظم وله سكربت تشغيل.
AvatarForge: منظم كـ profiles/docs.
```
