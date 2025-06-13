---
draft: false
date: 2025-06-01
categories:
    - gitlab
title: 'Our Gitlab migration is now underway'
authors:
  - asterisk
comments: true
description: "Here's what's changed."
---


![A black and white photo of several people walking along a barren landscape towards a mountain covered in mist.](../../assets/img/posts/migration/migration.jpg)
<small>Photo by <a href="https://unsplash.com/@sebastiengoldberg" target="_blank" rel="noopener noreferrer">Sébastien Goldberg</a> on <a href="https://unsplash.com/photos/people-walking-on-beach-during-daytime-AW5MxlFDVzc" target="_blank" rel="noopener noreferrer">Unsplash</a></small>

After a long wait, we've begun the migration process. 
All important repositories are on our Gitlab server, and push mirror to Github. 

<span class="orange">**Github PRs will no longer be accepted.** **Github Issues are depreceated and will be disabled across all repositories.**</span>

The Github repos will remain as read only mirrors for backup and discovery purposes.
<!-- more -->

## Why?

We need more control over our version control and issue tracking systems. This migration was always the plan, and had simply been delayed for a while.

With Gitlab, we don't have to rely on awful moderation tools or wait for some support team to ban spammers. We don't have to sign away our control to a company that could remove us or disappear at any time. We have full control over who can sign up, file issues and fork repos.

It's important for projects to take control of their resources together and move away from large centralized solutions, especially as Git forges are on the verge of becoming even more connected through [ForgeFed](https://forgefed.org/){ target="_blank" rel="noopener noreferrer" }. It's something we're finally following through with, and we've been preparing our instance for this. After [fixing the bot problem](gitlab-security.md) and setting up limits for new users, we're finally ready to take on some actual activity.

If you want to file an issue, [**sign up to our instance**](https://git.blendos.co/users/sign_up){ target="_blank" rel="noopener noreferrer" }.