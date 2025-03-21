---
layout: page
title: Blog
permalink: blog
---

<div class="custom-font">
  {% for post in site.posts %}
    <div class="py-0">
      <h3 class="!mb-1"><a class="dark:text-stone-300" href="{{site.baseurl}}{{ post.url }}">{{ post.title}}</a></h3>
      <div class="text-sm text-stone-400 dark:!text-slate-400 !mt-0">{{post.date | date: "%B %-d, %Y"}}</div>
    </div>
  {% endfor %}
</div>


