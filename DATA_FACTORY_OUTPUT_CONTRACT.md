# DATA_FACTORY_OUTPUT_CONTRACT.md

## لكل ملف داخل OUT/<file_id>/
- meta.json (إجباري)
- best.txt أو best.md (إن أمكن)
- best.norm.txt (إجباري للنصوص)
- tables/*.csv (إن وجدت)
- assets/ (صور/صفحات/فريمات/موجات…)

## meta.json (مقدس)
يجب أن يحتوي:
- source_path
- sha256
- detected_type + ext_mismatch
- router_decision (pipeline + pdf_mode إذا وجد)
- probes
- issues[]
- citations[] (page/row/line/timecode)
