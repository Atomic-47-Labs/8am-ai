#!/usr/bin/env python3
"""
EXP-0001 — Git Gists as a verifiable data substrate.
Source idea: IDEA-0332 (THEME-07 llm-evaluation-and-trust), grade 79.6.

The 8am AI group repeatedly floated using GitHub gists to emulate
blockchain-like verifiability: hash a payload, anchor it, and let anyone
re-verify later that the data is unchanged. This is a bounded, runnable
realization of that idea — no GitHub account required to demo, because the
"anchor" is content-addressed: the record id *is* the hash, so tampering is
detectable with nothing but the record itself.

Commands:
    anchor  <file>           -> emit a proof record (JSON) for the file
    verify  <file> <record>  -> check the file still matches the record
    sign    <file> <secret>  -> add an HMAC signature to a proof record
    check   <record> <secret>-> verify the HMAC signature

A real deployment would POST the proof record to a secret gist; the gist URL
becomes a timestamped, shareable anchor. The verifiability does not depend on
the gist — only on the SHA-256 — so the gist is convenience, not trust root.
"""
import sys, json, hashlib, hmac, time

def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

def anchor(path):
    digest = sha256_file(path)
    rec = {
        "v": 1,
        "alg": "sha-256",
        "file": path.split("/")[-1],
        "digest": digest,
        "bytes": _size(path),
        "anchored_at": int(time.time()),
        # content-addressed id: short prefix of the digest
        "id": "gist-" + digest[:16],
    }
    return rec

def _size(path):
    import os
    return os.path.getsize(path)

def verify(path, record):
    rec = _load(record)
    now = sha256_file(path)
    ok = (now == rec["digest"])
    return ok, rec["digest"], now

def sign(path, secret):
    rec = anchor(path)
    mac = hmac.new(secret.encode(), rec["digest"].encode(), hashlib.sha256).hexdigest()
    rec["hmac"] = mac
    return rec

def check(record, secret):
    rec = _load(record)
    if "hmac" not in rec:
        return False, "no hmac on record"
    expect = hmac.new(secret.encode(), rec["digest"].encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(expect, rec["hmac"]), rec["hmac"]

def _load(record):
    # record can be a path or an inline JSON string
    try:
        return json.loads(record)
    except json.JSONDecodeError:
        return json.load(open(record))

def main(argv):
    if len(argv) < 2:
        print(__doc__); return 1
    cmd = argv[1]
    if cmd == "anchor":
        print(json.dumps(anchor(argv[2]), indent=2))
    elif cmd == "verify":
        ok, want, got = verify(argv[2], argv[3])
        print(f"{'MATCH' if ok else 'TAMPERED'}  want={want[:16]}  got={got[:16]}")
        return 0 if ok else 2
    elif cmd == "sign":
        print(json.dumps(sign(argv[2], argv[3]), indent=2))
    elif cmd == "check":
        ok, mac = check(argv[2], argv[3])
        print(f"{'VALID' if ok else 'INVALID'}  hmac={mac[:16] if isinstance(mac,str) else mac}")
        return 0 if ok else 2
    else:
        print(__doc__); return 1
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
