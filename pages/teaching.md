---
layout: page
title: Teaching
permalink: teaching
---

<div class="custom-font flex flex-col gap-4 mt-4">
    {% for teaching in site.teachings reversed %}
    <div class="rounded-xl border border-stone-200 dark:border-stone-700 p-5 dark:bg-slate-900" key="{{ teaching.id }}">
        <div class="flex items-start justify-between gap-2 mb-2">
            <div>
                <h3 class="!mt-0 !mb-0 text-base md:!text-lg font-bold dark:text-stone-100">{{ teaching.course }}</h3>
                {% if teaching.description %}
                <p class="!mt-0.5 !mb-0 text-sm text-stone-500 dark:text-stone-400 italic">{{ teaching.description }}</p>
                {% endif %}
            </div>
            {% if teaching.position == "Lecturer" %}
            <span class="shrink-0 text-sm font-medium px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-200">{{ teaching.position }}</span>
            {% else %}
            <span class="shrink-0 text-sm font-medium px-2.5 py-0.5 rounded-full bg-stone-100 text-stone-700 dark:bg-slate-700 dark:text-stone-300">{{ teaching.position }}</span>
            {% endif %}
        </div>
        <p class="text-sm text-stone-400 dark:text-stone-500 !mt-0 !mb-0">{{ teaching.venue }}</p>
        {% if teaching.highlights %}
        <div style="max-height:0;overflow:hidden;transition:max-height 0.3s ease-in-out;">
            <ul class="!mt-2 !mb-0 !pl-4 space-y-0.5">
                {% for item in teaching.highlights %}
                <li class="text-sm text-stone-500 dark:text-stone-400 !my-0">{{ item }}</li>
                {% endfor %}
            </ul>
        </div>
        {% endif %}
        <div class="flex items-center justify-between mt-2">
            <p class="text-xs text-stone-400 dark:text-stone-500 !my-0">
                <i class="fas fa-calendar-alt mr-1"></i>{{ teaching.term }}
            </p>
            {% if teaching.highlights %}
            <button data-open="false" onclick="var o=this.dataset.open==='true';var c=this.parentElement.previousElementSibling;c.style.maxHeight=o?'0':c.scrollHeight+'px';this.dataset.open=o?'false':'true';this.textContent=o?'+ more':'− less';"
                class="text-xs text-stone-400 dark:text-stone-500 hover:text-stone-600 dark:hover:text-stone-300 cursor-pointer select-none bg-transparent border-none p-0">
                + more
            </button>
            {% endif %}
        </div>
    </div>
    {% endfor %}
</div>
