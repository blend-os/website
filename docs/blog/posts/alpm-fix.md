---
draft: false
date: 2025-12-13
categories:
  - akshara
title: "Emergency akshara fix for AUR updates"
authors:
  - asterisk
comments: false
description: "Emergency ALPM fix"
---

Run this instead of the normal `sudo akshara update`:

```bash
wget https://git.blendos.co/blendOS/system-tools/akshara/-/raw/main/akshara && sudo umount -l /usr && sudo mv ./akshara /usr/bin/akshara && sudo chmod +x /usr/bin/akshara && sudo akshara update
```

<!-- more -->
