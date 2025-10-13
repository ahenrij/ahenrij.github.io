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
                        <svg xmlns="http://www.w3.org/2000/svg" width="8" height="8" viewBox="0 0 10 10" class="ml-1 mt-1">
                            <path d="M7.849,15.54,14.76,8.629v2.988a.833.833,0,0,0,1.667,0v-5a.832.832,0,0,0-.833-.833h-5a.833.833,0,1,0,0,1.667h2.988L6.671,14.362A.833.833,0,0,0,7.849,15.54Z" transform="translate(-6.427 -5.784)" fill="currentColor"/>
                        </svg>
                    </a>
                    {% unless forloop.last %} {% endunless %}
                {% endfor %}
            </p>
        </div>
    </div>
    {% endfor %}
</div>
