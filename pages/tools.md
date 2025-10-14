---
layout: page
title: Tools
permalink: tools
---

<div class="custom-font">
    {% for tool in site.tools reversed %}
    <div class="mt-4 md:mt-8" key="{{ tool.id }}">
        <div class="flex flex-col space-y-0">
            <p class="text-base md:text-lg font-bold !my-0 dark:text-stone-100"><b>{{ tool.title }}</b> - {{ tool.description }}</p>
            <p class="text-sm md:text-base text-stone-500 dark:text-gray-400 ">{{ tool.authors }}</p>
            <p class="text-[.8rem] md:text-[1rem] text-gray-400 -mt-1">
                <span>{{ tool.venue }}</span>
                {% for link in tool.links %}
                    <a href="{{ link.url }}" target="_blank" class="inline-flex items-center text-base mr-2 !no-underline hover:!underline">
                        {{ link.name }}
                        {% include arrow-ne.html %}
                    </a>
                    {% unless forloop.last %} {% endunless %}
                {% endfor %}
            </p>
        </div>
    </div>
    {% endfor %}
</div>
