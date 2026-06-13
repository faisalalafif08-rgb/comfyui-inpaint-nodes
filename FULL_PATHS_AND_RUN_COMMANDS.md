# شجرة المسارات الكاملة وطريقة التشغيل

## الجذر
```text
D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612
```

## جدول التشغيل
| النظام/المجلد | المسار الكامل | طريقة التشغيل | الرابط |
|---|---|---|---|
| Workspace Root | $(System.Collections.Hashtable.Path) | $(System.Collections.Hashtable.Run) |  |
| Archives Original | $(System.Collections.Hashtable.Path) | $(System.Collections.Hashtable.Run) |  |
| Fooocus Main Canonical | $(System.Collections.Hashtable.Path) | $(System.Collections.Hashtable.Run) | http://127.0.0.1:7869 / الجوال: http://192.168.3.16:7869 |
| Fooocus Entry With Update Full | $(System.Collections.Hashtable.Path) | $(System.Collections.Hashtable.Run) | http://127.0.0.1:7871 / الجوال: http://192.168.3.16:7871 |
| Fooocus Release Minimal | $(System.Collections.Hashtable.Path) | $(System.Collections.Hashtable.Run) | حسب البورت داخل السكربت |
| Female Prompt Pack | $(System.Collections.Hashtable.Path) | $(System.Collections.Hashtable.Run) |  |
| Stable Diffusion WebUI | $(System.Collections.Hashtable.Path) | $(System.Collections.Hashtable.Run) | http://127.0.0.1:7870 / الجوال: http://192.168.3.16:7870 |
| Shared Outputs | $(System.Collections.Hashtable.Path) | $(System.Collections.Hashtable.Run) |  |
| Stable Diffusion API Probe Output | $(System.Collections.Hashtable.Path) | $(System.Collections.Hashtable.Run) |  |
| Run Scripts | $(System.Collections.Hashtable.Path) | $(System.Collections.Hashtable.Run) |  |
| Reports | $(System.Collections.Hashtable.Path) | $(System.Collections.Hashtable.Run) |  |
| Portable Tools | $(System.Collections.Hashtable.Path) | $(System.Collections.Hashtable.Run) |  |
| ALZaeem Windows Ready | $(System.Collections.Hashtable.Path) | $(System.Collections.Hashtable.Run) |  |
| AvatarForge | $(System.Collections.Hashtable.Path) | $(System.Collections.Hashtable.Run) |  |

## شجرة مختصرة
```text
D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612
├── 00_archives_original
├── 01_fooocus
│   ├── Fooocus-main_canonical\Fooocus-main
│   ├── entry_with_update_full
│   ├── Fooocus-release_minimal\Fooocus-release
│   └── female_prompt_pack\Fooocus_Female_System_Windows
├── 02_stable_diffusion_webui
│   └── stable-diffusion-webui-master\stable-diffusion-webui-master
├── 03_shared_models_and_outputs
│   └── stable_diffusion_api_probe
├── 04_run_scripts
├── 05_docs_reports
├── 06_portable_tools
├── 07_alzaeem_windows_ready
│   └── ALZaeem_Windows_Ready
└── 08_avatarforge
```

## أهم أوامر التشغيل الآن

### Fooocus الأساسي
```powershell
& "D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\04_run_scripts\run_fooocus_main_canonical.bat"
```

### Fooocus البديل entry_with_update
```powershell
& "D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\04_run_scripts\run_fooocus_entry_with_update_full_no_update.bat"
```

### Stable Diffusion WebUI API
```powershell
powershell -ExecutionPolicy Bypass -File "D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\04_run_scripts\run_stable_diffusion_webui_api_direct.ps1"
```

### ALZaeem
```powershell
& "D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\04_run_scripts\run_alzaeem_windows_ready.bat"
```

## روابط الجوال
```text
Fooocus الأساسي: http://192.168.3.16:7869
Stable Diffusion: http://192.168.3.16:7870
Fooocus البديل: http://192.168.3.16:7871
```
