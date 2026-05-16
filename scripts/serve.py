#!/usr/bin/env python3
"""Serve the generated static blog locally."""

from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import argparse
import os


ROOT = Path(__file__).resolve().parents[1]


class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


def main():
    parser = argparse.ArgumentParser(description="Serve the static blog.")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=4000, type=int)
    args = parser.parse_args()

    os.chdir(ROOT)
    server = ThreadingHTTPServer((args.host, args.port), NoCacheHandler)
    print(f"Serving {ROOT} at http://{args.host}:{args.port}/")
    server.serve_forever()


if __name__ == "__main__":
    main()
