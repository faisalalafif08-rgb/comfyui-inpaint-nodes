# -*- coding: utf-8 -*-
import sys
import time
from pathlib import Path
import requests
from gradio_client import Client

BASE = Path(r"D:\zzipp\جي بي\الكميرا\_organized_generation_workspace_20260612")
APP = BASE / "01_fooocus" / "Fooocus-main_canonical" / "Fooocus-main"
OUT_DIR = APP / "outputs"

cfg = requests.get("http://127.0.0.1:7869/config", timeout=10).json()
components = {c["id"]: c for c in cfg["components"]}
inputs_ids = cfg["dependencies"][67]["inputs"]

def default_value(component_id):
    c = components[component_id]
    typ = c.get("type")
    props = c.get("props", {})
    if typ == "state":
        return None
    return props.get("value")

payload = [default_value(cid) for cid in inputs_ids]
# Minimal text-to-image test.
payload[0] = None
payload[1] = False
payload[2] = "a realistic red apple on a wooden table, studio lighting, sharp focus"
payload[3] = ""
payload[5] = "Speed"
payload[7] = 1
payload[8] = "png"
payload[9] = "12345"
# Disable all LoRA slots: indexes 16..30 = enable,name,weight repeated.
for idx in (16, 19, 22, 25, 28):
    payload[idx] = False
for idx in (17, 20, 23, 26, 29):
    payload[idx] = "None"
for idx in (18, 21, 24, 27, 30):
    payload[idx] = 1.0
# No input image, no previews, force a very small smoke-test generation.
payload[31] = False
payload[39] = True
payload[40] = True
payload[41] = True
payload[42] = False
payload[51] = 15
payload[53] = 512
payload[54] = 512
payload[78] = False
payload[79] = False

before = {str(p): p.stat().st_mtime for p in OUT_DIR.rglob("*.png")} if OUT_DIR.exists() else {}
print("BEFORE_PNG", len(before))
client = Client("http://127.0.0.1:7869")
print("CLIENT_READY")
print("ENDPOINT67_USE_WS", getattr(client.endpoints[67], "use_ws", None))
print("ENDPOINT68_USE_WS", getattr(client.endpoints[68], "use_ws", None))
client_payload = [value for component_id, value in zip(inputs_ids, payload) if components[component_id].get("type") != "state"]
print("PAYLOAD_LEN", len(payload), "CLIENT_PAYLOAD_LEN", len(client_payload))
# Step matching the Generate button chain: create task state, then run task.
print("CALL_FN67_CREATE_TASK")
res67 = client.predict(*client_payload, fn_index=67)
print("FN67_RESULT", type(res67).__name__, repr(res67)[:1000])
print("CALL_FN68_RUN_TASK")
job = client.submit(fn_index=68)
print("FN68_JOB_SUBMITTED")
try:
    res68 = job.result(timeout=900)
    print("FN68_RESULT", type(res68).__name__, repr(res68)[:2000])
except Exception as exc:
    # Fooocus saves the image before gradio_client tries to deserialize the
    # gallery result, which can be returned as a dict by this Gradio version.
    print("FN68_RESULT_READ_ERROR", type(exc).__name__, repr(exc)[:1000])
for i in range(240):
    after_files = list(OUT_DIR.rglob("*.png")) if OUT_DIR.exists() else []
    new_files = [p for p in after_files if str(p) not in before]
    if new_files:
        newest = sorted(new_files, key=lambda p: p.stat().st_mtime, reverse=True)[0]
        print("GENERATED_FILE", newest)
        print("GENERATED_SIZE", newest.stat().st_size)
        sys.exit(0)
    time.sleep(1)
print("NO_GENERATED_FILE")
sys.exit(2)
