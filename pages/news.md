---
layout: page
title: News
permalink: news
---

<style>
  .news-feed a, .news-feed .link { color: #57534e; font-weight: 500; text-decoration: underline; text-decoration-color: #d6d3d1 !important; text-decoration-thickness: 1px; text-underline-offset: 3px; transition: color 0.2s ease, text-decoration-color 0.2s ease; }
  .news-feed a:hover, .news-feed .link:hover { color: #1c1917; text-decoration-color: #a8a29e !important; }
  .dark .news-feed a, .dark .news-feed .link { color: #d6d3d1; text-decoration-color: #57534e !important; }
  .dark .news-feed a:hover, .dark .news-feed .link:hover { color: #fafaf9; text-decoration-color: #a8a29e !important; }
</style>

{% assign sorted_news = site.news | sort: "date" | reverse %}
<div class="not-prose custom-font news-feed space-y-0 mt-4">
  {% for item in sorted_news %}
    {% if item.category == "paper" %}{% assign label = "Paper" %}
    {% elsif item.category == "award" %}{% assign label = "Award" %}
    {% elsif item.category == "position" %}{% assign label = "Position" %}
    {% elsif item.category == "talk" %}{% assign label = "Talk" %}
    {% elsif item.category == "tool" %}{% assign label = "Tool" %}
    {% else %}{% assign label = "News" %}{% endif %}
    <div class="flex gap-4 py-4" style="border-bottom: 1px solid rgba(120,113,108,0.12);">
      <div class="pt-0.5 shrink-0 text-stone-700 dark:text-stone-200">
        {% include news-icon.html category=item.category %}
      </div>
      <div class="flex-1 min-w-0">
        <div class="flex items-center gap-2 mb-1.5">
          <span class="text-xs font-bold uppercase tracking-wider text-stone-700 dark:text-stone-200">{{ label }}</span>
          <span class="text-xs font-mono text-stone-300 dark:text-stone-600">{{ item.date | date: "%b %Y" }}</span>
        </div>
        <div class="text-base dark:text-stone-300 text-stone-600 mb-0 leading-relaxed">{{ item.content }}</div>
      </div>
    </div>
  {% endfor %}
</div>
