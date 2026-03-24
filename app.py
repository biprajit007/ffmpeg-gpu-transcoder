#!/usr/bin/env python3
"""Run GPU-accelerated encodes and collect benchmark results."""
import argparse, json, shutil, subprocess, time

def require(x):
    if shutil.which(x) is None: raise SystemExit(f'Missing required binary: {x}')

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('input'); p.add_argument('output'); p.add_argument('--encoder',default='h264_videotoolbox'); p.add_argument('--dry-run',action='store_true')
    a=p.parse_args(); require('ffmpeg')
    cmd=['ffmpeg','-y','-i',a.input,'-c:v',a.encoder,'-b:v','4M','-c:a','aac',a.output]
    print(' '.join(cmd))
    if a.dry_run: return
    t=time.time(); subprocess.check_call(cmd); print(json.dumps({'seconds': round(time.time()-t,2), 'encoder': a.encoder}, indent=2))
if __name__ == '__main__': main()
