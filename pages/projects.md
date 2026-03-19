---
layout: page
title: Projects
permalink: projects
---

<div class="custom-font grid grid-cols-1 md:grid-cols-2 gap-4 md:gap-6 mt-4">
    {% for project in site.projects reversed %}
    <div class="flex flex-col justify-between rounded-xl border border-stone-200 dark:border-stone-700 p-5 hover:shadow-md transition-shadow duration-200 dark:bg-slate-900" key="{{ project.id }}">
        <div>
            <div class="flex items-start justify-between gap-2 mb-1">
                <h3 class="!mt-0 !mb-0 text-base md:!text-lg font-bold dark:text-stone-100">{{ project.title }}</h3>
                <span class="text-xs text-stone-400 dark:text-stone-500 shrink-0 pt-1">{{ project.year }}</span>
            </div>
            <p class="text-sm md:text-base text-stone-600 dark:text-stone-300 mt-1 !mb-0">{{ project.description }}</p>
            <p class="text-xs text-stone-400 dark:text-stone-500 !mt-0.5 mb-0">{{ project.authors }}</p>
            {% if project.venue %}
            <p class="text-xs text-stone-500 dark:text-stone-400 mt-2 mb-0 italic">{{ project.venue }}</p>
            {% endif %}
        </div>
        {% if project.links %}
        <div class="flex flex-wrap gap-2 mt-2">
            {% for link in project.links %}
            <a href="{{ link.url }}" target="_blank" class="inline-flex items-center gap-1 text-xs px-2.5 py-1 rounded-full border border-stone-300 dark:border-stone-600 text-stone-600 dark:text-stone-300 hover:bg-stone-100 dark:hover:bg-slate-700 !no-underline transition-colors duration-150">
                {{ link.name }}
                {% include arrow-ne.html %}
            </a>
            {% endfor %}
        </div>
        {% endif %}
    </div>
    {% endfor %}
</div>
