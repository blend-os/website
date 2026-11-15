---
draft: false
date: 2026-11-15
categories:
  - akshara
  - problems
title: 'Manual akshara upgrade required to fix OpenSSL 4 issues'
authors:
  - asterisk
comments: true
description: ''
# discuss:
#  subreddit: ''
---
In order to fix issues with the OpenSSL 4 update, you need to download the development version of akshara from our Gitlab:

```bash
wget "https://git.blendos.co/blendOS/system-tools/akshara/-/raw/main/akshara" && chmod +x akshara
```

Then, whenever you need to run akshara do:

```bash
sudo python ./akshara update
```

You'll only need to do this until the `akshara` package is updated.

<!-- more -->
