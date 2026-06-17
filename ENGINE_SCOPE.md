# comfyui-inpaint-nodes

## الدور الرسمي داخل منظومة الزعيم

هذا المستودع ليس قاعدة النظام العامة، وليس مكان الشخصيات أو قواعد اللغة.

دوره هو:

```text
Visual Engine / Inpaint Tools Reference
```

يعني يحتفظ بأدوات الصورة والـ inpaint والـ outpaint وما يرتبط بمحركات الرؤية والإنتاج.

## علاقته بالنظام

يسجل داخل:

```text
C:\unified_ai_system\09_registry\visual_engines_registry.json
```

ويتعامل معه النظام كـ Adapter/Capability، وليس كقلب النظام.

## لا يوضع هنا

```text
قواعد SQLite العامة
ملفات PDF/OCR
ذاكرة Gold/Silver/Bronze
مشاريع Project Factory
موديلات ضخمة
outputs
venv/.venv
```

## القاعدة

```text
engine_reference_only = true
run_through_adapter_only = true
review_required = true
gold_write = false
```
