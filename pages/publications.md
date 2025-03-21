---
layout: page
title: Publications
permalink: publications
---

<div class="custom-font">
    {% for pub in site.publications reversed %}
    <div class="mt-4 md:mt-8" key="{{ pub.id }}">
        <div class="flex space-x-4 md:space-x-8">
            <div class="text-base font-bold text-stone-700 md:text-lg">{{ pub.year }}</div>
            <div class="flex flex-col space-y-0">
                {% if pub.link == "" %}
                    <p class="text-base md:text-lg font-bold !my-0">{{ pub.title }}</p>
                {% else %}
                    <p class="text-base md:text-lg font-bold !my-0"><a href="{{ pub.link }}" target="_blank">{{ pub.title }}</a></p>
                {% endif %}
                <p class="text-base md:text-lg text-stone-500">{{ pub.authors }}</p>
                <p class="text-[.8rem] md:text-[1rem] text-gray-400 -mt-1">{{ pub.venue }}</p>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
