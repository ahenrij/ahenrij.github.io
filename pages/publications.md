---
layout: page
title: Publications
permalink: publications
---

<div class="custom-font">
    {% for pub in site.publications reversed %}
    <div class="mt-4 md:mt-8" key="{{ pub.id }}">
        <div class="flex space-x-4 md:space-x-8">
            <div class="text-base md:text-lg font-bold text-stone-700 dark:text-stone-100">{{ pub.date | date: "%Y" }}</div>
            <div class="flex flex-col space-y-0">
                <p class="text-base md:text-lg font-bold !my-0 dark:text-stone-100">{{ pub.title }}</p>
                <p class="text-base md:text-lg text-stone-500 dark:text-stone-300 ">{{ pub.authors }}</p>
                <p class="text-[.8rem] md:text-[1rem] text-gray-400 -mt-1">
                    <span>{{ pub.venue }}</span>
                    {% for link in pub.links %}
                        <a href="{{ link.url }}" target="_blank" class="inline-flex items-center text-whitepx-4 text-base ml-1 !no-underline hover:!underline">
                            {{ link.name }}
                            {% include arrow-ne.html %}
                        </a>
                        {% unless forloop.last %} {% endunless %}
                    {% endfor %}
                </p>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
