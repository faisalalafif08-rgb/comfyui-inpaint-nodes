# الشجرة الكاملة وكل الملفات

هذا الجرد يشمل كل شيء داخل مجلد التنظيم، حتى الملفات التي لم نستخدمها أو لم نشغلها.

## الجذر

```text
D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612
```

## ملفات الجرد

| الملف | ماذا يحتوي |
|---|---|
| `FULL_ALL_FILES_INVENTORY.csv` | كل الملفات، المسار الكامل، المسار النسبي، الاسم، الامتداد، الحجم، آخر تعديل |
| `FULL_DIRECTORY_TREE.txt` | كل المجلدات كشجرة نصية كاملة |
| `TOP_LEVEL_COUNTS_ALL.csv` | ملخص كل مجلد رئيسي: عدد الملفات، عدد المجلدات، الحجم |
| `FULL_PATHS_AND_RUN_COMMANDS.md` | المسارات المهمة وطريقة التشغيل |
| `fooocus_entry_with_update_full_scene_map.md` | خريطة Fooocus البديل للمشاهد |

## الأرقام الحالية

```text
Total files: 96435
Total directories: 9678
```

## طريقة الاستخدام

لو تبغى تبحث عن ملف:

```powershell
Import-Csv "D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\05_docs_reports\FULL_ALL_FILES_INVENTORY.csv" |
Where-Object { $_.Name -like "*اسم_الملف*" } |
Select-Object relative_path, full_path, Length
```

لو تبغى تبحث عن موديلات:

```powershell
Import-Csv "D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\05_docs_reports\FULL_ALL_FILES_INVENTORY.csv" |
Where-Object { $_.Extension -in ".safetensors", ".ckpt", ".pt", ".bin" } |
Select-Object relative_path, Length
```

لو تبغى تعرف كل سكربتات التشغيل:

```powershell
Import-Csv "D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\05_docs_reports\FULL_ALL_FILES_INVENTORY.csv" |
Where-Object { $_.Extension -in ".bat", ".ps1", ".py" -and $_.relative_path -like "04_run_scripts*" } |
Select-Object relative_path, full_path
```
