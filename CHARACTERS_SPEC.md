# CHARACTERS_SPEC.md

## الفكرة
الشخصية تتطور: نص → صوت → أفاتار ثابت → أفاتار متحرك → ممثل مشاهد (سينما).

## Character Contract
لكل شخصية ملف ثابت:
`C:\XTTS\characters\<Name>\character.json`

### حقول أساسية
- name
- dialect: lebanese / hijazi / ...
- voice_profile: Amal / Maya / Fno
- style_presets: 2-3 أساليب
- avatar: path + type
- video_actor: engine + settings (لاحقًا)
- safety/consent: سياسة الاستنساخ

## الربط
Character = Voice + Style + Policy
- تغيير style لا يغير الصوت
- تغيير الصوت لا يغير أسلوب النظام العام إلا إذا ربطته بالشخصية
