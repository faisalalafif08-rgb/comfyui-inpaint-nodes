# خريطة Fooocus entry_with_update_full للمشاهد

المجلد:
```text
D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\01_fooocus\entry_with_update_full
```

التشغيل:
```text
D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\04_run_scripts\run_fooocus_entry_with_update_full_no_update.bat
```

الرابط المحلي/الجوال بعد --listen:
```text
http://127.0.0.1:7871
http://192.168.3.16:7871
```

## جدول مجلدات النظام

| المجلد | عدد الملفات | الحجم GB | ماذا يفعل | هل يهم للمشاهد؟ |
|---|---:|---:|---|---|
| css | 1 | 0 | ستايل واجهة Fooocus | مساند |
| extras | 64 | 0.001 | أدوات إضافية مثل BLIP/interrogate/faces/IP-Adapter/preprocessors | نعم للأدوات المساعدة |
| input | 0 | 0 | مدخلات الصور لو تستخدم image prompt أو inpaint | نعم عند استخدام صور مرجعية |
| javascript | 7 | 0 | سكربتات الواجهة | مساند |
| language | 2 | 0 | ملفات لغة الواجهة | مساند |
| ldm_patched | 226 | 0.004 | محرك النماذج والـ diffusion والـ samplers المعدلة | تشغيلي مهم |
| models | 48 | 9.818 | كل الموديلات: checkpoints/loras/controlnet/clip_vision/upscale | نعم، أهم شيء |
| modules | 67 | 0.001 | منطق Fooocus: الواجهة، التوليد، إدارة الإعدادات | تشغيلي |
| outputs | 0 | 0 | مكان الصور الناتجة من هذه النسخة | نعم، هنا النتيجة |
| presets | 9 | 0 | إعدادات جاهزة/أنماط تشغيل مسبقة | نعم، يسرع الإعداد |
| sdxl_styles | 285 | 0.007 | ستايلات جاهزة للمشهد مثل cinematic/anime/photo | نعم، يساعد شكل المشهد |
| wildcards | 8 | 0 | قوائم كلمات عشوائية للبرومبتات | مساند |

## مجلد models بالتفصيل

| models subfolder | عدد الملفات | الحجم GB | يستخدم في |
|---|---:|---:|---|
| checkpoints | 2 | 6.617 | الموديل الأساسي الذي يرسم المشاهد |
| clip | 1 | 0 | CLIP نصي إن وجد |
| clip_vision | 3 | 1.837 | فهم الصور المرجعية وImage Prompt |
| configs | 11 | 0 | تعريفات تكوين الموديلات |
| controlnet | 3 | 0.944 | تحكم بالصورة/الوضعية/IP Adapter |
| diffusers | 1 | 0 | مساند/احتياطي |
| embeddings | 2 | 0 | تعزيزات نصية/negative embeddings |
| gligen | 1 | 0 | مساند/احتياطي |
| hypernetworks | 1 | 0 | مساند/احتياطي |
| inpaint | 1 | 0 | إصلاح مناطق داخل صورة |
| loras | 2 | 0.046 | تعديل أسلوب/شخصية/تفاصيل فوق الموديل |
| prompt_expansion | 9 | 0.33 | توسيع البرومبت تلقائيًا |
| safety_checker | 1 | 0 | مساند/احتياطي |
| sam | 0 | 0 | مساند/احتياطي |
| style_models | 1 | 0 | مساند/احتياطي |
| unet | 1 | 0 | مساند/احتياطي |
| upscale_models | 2 | 0.031 | تكبير وتحسين الصورة |
| vae | 1 | 0 | VAE إضافي إن وجد |
| vae_approx | 5 | 0.012 | معاينة/فك ترميز أسرع |

## ملفات الموديل الأساسية

### Checkpoints
| الملف | الحجم GB | المسار |
|---|---:|---|
| juggernautXL_v8Rundiffusion.safetensors | 6.617 | D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\01_fooocus\entry_with_update_full\models\checkpoints\juggernautXL_v8Rundiffusion.safetensors |
| put_checkpoints_here | 0 | D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\01_fooocus\entry_with_update_full\models\checkpoints\put_checkpoints_here |

### LoRA
| الملف | الحجم MB | المسار |
|---|---:|---|
| put_loras_here | 0 | D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\01_fooocus\entry_with_update_full\models\loras\put_loras_here |
| sd_xl_offset_example-lora_1.0.safetensors | 47.26 | D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612\01_fooocus\entry_with_update_full\models\loras\sd_xl_offset_example-lora_1.0.safetensors |

## استخدامه للمشاهد الآن

| الحاجة | تستخدم ماذا؟ | النتيجة |
|---|---|---|
| توليد مشهد جديد | Prompt داخل واجهة Fooocus على 7871 | صورة في outputs |
| الحفاظ على شخصية/ستايل | LoRA أو prompt ثابت + seed ثابت | اتساق أعلى بين المشاهد |
| مشهد من صورة مرجعية | input + image prompt / clip_vision / controlnet | صورة قريبة من المرجع |
| تحسين صورة | upscale_models | نسخة أكبر/أوضح |
| أسلوب سينمائي سريع | sdxl_styles + presets | شكل جاهز للمشهد |
| حفظ النتائج | outputs | كل مخرجات النسخة البديلة |

## قرار الاستخدام

هذه النسخة بديلة/احتياطية جيدة للمشاهد، خصوصًا إذا احتجت موديلات أو إعدادات غير موجودة في Fooocus-main_canonical. لكنها ليست الأساسية إلا إذا أردت اختبار فرق النتائج بينها وبين النسخة الرئيسية.
