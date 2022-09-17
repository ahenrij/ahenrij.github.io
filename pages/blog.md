---
layout: page
title: Blog
permalink: blog
---

<div>
  {% for post in site.posts %}
    <div class="py-1">
      <h3><a class="dark:text-stone-300" href="{{site.baseurl}}{{ post.url }}">{{ post.title}}</a></h3>
      <div class="text-sm text-stone-400">{{post.date | date: "%B %-d, %Y"}}</div>
    </div>
  {% endfor %}
</div>


