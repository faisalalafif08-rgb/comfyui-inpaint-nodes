# DATA_FACTORY_ROUTER_SPEC.md

## 0) الهدف
أي ملف يدخل `data/INPUT` لازم يمر بثلاث مراحل: Filter → Probe → Route، ثم يطلع نواتج موحّدة داخل `data/OUT/<file_id>/`.

## 1) Filter Rules
### 1.1 Path Ignore
يتجاهل تلقائيًا: `.git/`, `node_modules/`, `__pycache__/`, `venv/`, `.venv/`, `dist/`, `build/`, `.next/`, `obj/`, `bin/`, `tmp/`, `cache/`.

### 1.2 Size
- `size==0` → skip  
- `size>MAX_SIZE` → queue + meta reason

### 1.3 Magic Bytes
تحديد النوع الحقيقي من header، وتسجيل `ext_mismatch` عند اختلاف الامتداد.

### 1.4 Binary Detector
قراءة 32KB: إذا كثرت أحرف التحكم/NULL → binary → skip أو assets-only.

## 2) Probes
- `type_guess`
- `encoding_guess`
- `language_mix`
- `has_tables`
- `has_code`
- `layout_complex`
- `is_scanned` (PDF)
- `content_density`

## 3) Pipelines
TEXT / CODE / TABLE_DIGITAL / OFFICE / ARCHIVE / IMAGE_OCR / AUDIO / VIDEO

## 4) PDF Modes (8)
PDF_DIGITAL_TEXT / PDF_SCANNED_OLD / PDF_SCANNED_TABLES / PDF_DIGITAL_TABLES / PDF_MIXED_LANGUAGE / PDF_CODE_HEAVY / PDF_LAYOUT_COMPLEX / PDF_SLIDES_IMAGE_ONLY

## 5) Output Contract
`meta.json`, `best.txt|best.md`, `best.norm.txt`, `tables/`, `assets/`

## 6) Chunking
Text chars-chunks / Code line-chunks / Tables row-chunks / PDF page-chunks / AV time-chunks

## 7) Non-goals
لا تعديل على الأصل، لا OCR للجميع بلا حاجة، لا فهرسة binaries كنص.
