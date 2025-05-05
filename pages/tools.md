---
layout: page
title: Tools
permalink: tools
---

<div class="custom-font">
    {% for tool in site.tools reversed %}
    <div class="mt-4 md:mt-8" key="{{ tool.id }}">
        <div class="flex flex-col space-y-0">
            <p class="text-base md:text-lg font-bold !my-0"><a href="{{ tool.link }}" target="_blank" class="!no-underline !font-bold hover:!underline !transition-all !duration-500 !ease-in-out">{{ tool.title }}</a></p>
            <p class="text-sm md:text-base text-stone-500 dark:text-gray-400 ">{{ tool.authors }}</p>
        </div>
    </div>
    {% endfor %}
</div>
