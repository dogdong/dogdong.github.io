# dogdong.github.io

This repository contains the generated static files for the blog published by GitHub Pages.

## Local Preview

Run a local static server from the repository root:

```bash
python3 scripts/serve.py
```

Then open:

```text
http://127.0.0.1:4000/
```

Use another port if needed:

```bash
python3 scripts/serve.py --port 4001
```

## Update Flow

This repo is the generated site, not the original Hexo source project. It does not currently contain:

- `_config.yml`
- `package.json`
- `source/_posts`
- theme source files

For normal blog writing, keep a separate Hexo source project under Git, write Markdown posts in `source/_posts`, run `hexo generate`, then publish the generated files to this repository.

For small direct edits to the already generated site:

```bash
git status
python3 scripts/serve.py
git add -u
git commit -m "Update blog"
git push origin master
```

Avoid committing IDE files such as `.idea/`.
