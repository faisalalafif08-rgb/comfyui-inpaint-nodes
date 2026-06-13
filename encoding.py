# -*- coding: utf-8 -*-
from typing import Tuple
ENCODINGS_TRY = ("utf-8","utf-8-sig","cp1256","iso-8859-6")
def smart_read_text(path, max_chars: int=2_000_000) -> Tuple[str,str,list]:
    issues=[]
    data = path.read_bytes()
    for enc in ENCODINGS_TRY:
        try:
            return data.decode(enc)[:max_chars], enc, issues
        except Exception:
            continue
    issues.append("encoding_fallback_ignore")
    return data.decode("utf-8", errors="ignore")[:max_chars], "utf-8(ignore)", issues
