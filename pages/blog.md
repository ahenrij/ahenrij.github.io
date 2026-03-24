---
layout: page
title: Blog
permalink: blog
---

<div class="not-prose custom-font space-y-4 mt-4">
  {% for post in site.posts %}
    <div class="theme-card rounded-lg p-4">
      <h3 class="font-semibold text-base dark:text-stone-100 mb-1 mt-0">
        <a class="link" href="{{site.baseurl}}{{ post.url }}">{{ post.title }}</a>
      </h3>
      <div class="text-xs text-stone-400 dark:text-stone-500 mb-2">{{post.date | date: "%B %-d, %Y"}}</div>
      {% if post.tags.size != 0 %}
        <div class="flex flex-wrap gap-1">
          {% for tag in post.tags %}
            <span class="inline-flex items-center px-2 py-0.5 rounded-full text-xs font-medium bg-stone-100 dark:bg-dark-elevated text-stone-600 dark:text-stone-400">{{ tag }}</span>
          {% endfor %}
        </div>
      {% endif %}
    </div>
  {% endfor %}
</div>
