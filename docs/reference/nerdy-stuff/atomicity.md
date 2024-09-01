---
icon: material/atom
description: Technical details for atomicity and updates
---

# :material-atom: Atomicity

First, an important detail:

- Updates are **indivisible transactions**. They must fail or succeed as one, they can never be partially complete.

An example of this is a bookstore. If you try to buy a book with counterfeit money, the transaction will fail. If the book cannot be found, the transaction fails. In both cases you don't get a book.

If all is well however, you get the book and move on. The book transaction can never be partially complete. It has either failed or succeeded.

Therefore:

- **If an update fails, it is abandoned and never applied.**

This transactional approach is called **atomicity**.

Every update is applied at boot using an `initramfs` hook through `mkinitcpio`.

The process works like this:

1. The base filesystem is downloaded from the Arch mirrors and extracted.
2. Packages from specified “track” in /system.yaml are installed, and custom commands are executed. At this point a second system has been created and is being manipulated.
3. This new filesystem replaces your current one on the next boot.
