---
layout: page
title: Teaching
permalink: teaching
---

<div class="custom-font not-prose flex flex-col gap-3 mt-4">
    {% for teaching in site.teachings reversed %}
    <div class="theme-card rounded-lg p-4" key="{{ teaching.id }}">
        <div class="flex items-start justify-between gap-2 mb-1">
            <div>
                <p class="!mt-0 !mb-0 text-base font-semibold dark:text-stone-100">{{ teaching.course }}</p>
                {% if teaching.description %}
                <p class="!mt-0.5 !mb-0 text-sm font-medium text-emerald-600 dark:text-dark-accent">{{ teaching.description }}</p>
                {% endif %}
            </div>
            {% if teaching.position == "Lecturer" %}
            <span class="theme-tag shrink-0 text-xs font-medium px-2 py-0.5 rounded-full">{{ teaching.position }}</span>
            {% else %}
            <span class="shrink-0 text-xs font-medium px-2 py-0.5 rounded-full bg-stone-100 text-stone-600 dark:bg-slate-700 dark:text-stone-400">{{ teaching.position }}</span>
            {% endif %}
        </div>
        <p class="text-sm text-stone-400 dark:text-stone-500 !mt-0 !mb-0">{{ teaching.venue }}</p>
        <p class="text-xs text-stone-400 dark:text-stone-500 !mt-2 !mb-0 flex items-center gap-1.5">
            <svg width="12" height="12" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="12" height="11" rx="1.5"/><line x1="2" y1="7" x2="14" y2="7"/><line x1="5.5" y1="1.5" x2="5.5" y2="4.5"/><line x1="10.5" y1="1.5" x2="10.5" y2="4.5"/></svg>
            {{ teaching.term }}
        </p>
    </div>
    {% endfor %}
</div>
