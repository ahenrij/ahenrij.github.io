---
layout: page
title: Tools
permalink: tools
---

<div class="custom-font">
    {% for tool in site.tools reversed %}
    <div class="mt-4 md:mt-8" key="{{ tool.id }}">
        <div class="flex space-x-4 md:space-x-8">
            <div class="text-base font-bold text-stone-700 dark:text-stone-100 md:text-lg">{{ tool.year }}</div>
            <div class="flex flex-col space-y-0">
                {% if pub.link == "" %}
                    <p class="text-base md:text-lg font-bold !my-0 dark:text-stone-300">{{ tool.title }}</p>
                {% else %}
                    <p class="text-base md:text-lg font-bold !my-0"><a href="{{ tool.link }}" target="_blank">{{ tool.title }}</a></p>
                {% endif %}
                <p class="text-base md:text-lg text-stone-500 dark:text-stone-300 ">{{ tool.authors }}</p>
                <p class="text-[.8rem] md:text-[1rem] text-gray-400 -mt-1">{{ tool.venue }}</p>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
