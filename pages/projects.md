---
layout: page
title: Projects
permalink: projects
---

<div class="custom-font grid grid-cols-1 md:grid-cols-2 gap-5 mt-4" style="width:min(1000px, calc(100vw - 2rem)); margin-left:calc((min(1000px, calc(100vw - 2rem)) - 100%) / -2);">
    {% for project in site.projects reversed %}
    <div class="theme-card project-card theme-card-hover flex flex-col rounded-xl overflow-hidden transition-shadow duration-200">
        <!-- Image -->
        <div class="project-img-bg relative w-full">
            {% if project.image %}
            {% assign img_path = '/assets/img/project/' | append: project.image %}
            <img src="{{ site.baseurl }}{{ img_path }}"
                 alt="{{ project.title }}"
                 class="w-full h-full object-cover block !my-0"
                 onerror="this.style.display='none'">
            <div class="absolute inset-0" style="background:rgba(0, 0, 0, 0.05);"></div>
            {% endif %}
        </div>
        <!-- Content -->
        <div class="flex flex-col flex-1 px-5 py-4">
            <h3 class="!-mt-1 !mb-1 text-lg font-bold dark:text-stone-100 leading-snug">{{ project.title }}</h3>
            <p class="text-sm md:text-base text-stone-600 dark:text-stone-300 !mt-0 !mb-1">
            {{ project.description }}
            {% if project.venue %}
            <span class="text-xs text-stone-500 dark:text-stone-400 !mt-0 !mb-0"> · {{ project.venue }}</span>
            {% endif %}    
            </p>
            {% if project.links %}
            <div class="flex flex-wrap gap-2 mt-2 -ml-1">
                {% for link in project.links %}
                <a href="{{ link.url }}" target="_blank" class="theme-link-pill inline-flex items-center gap-1 text-xs px-2.5 py-1 rounded-full !no-underline transition-colors duration-150">
                    {{ link.name }}
                    {% include arrow-ne.html %}
                </a>
                {% endfor %}
            </div>
            {% endif %}
        </div>
    </div>
    {% endfor %}
</div>
