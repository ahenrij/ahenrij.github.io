---
layout: page
title: Publications
permalink: publications
---

<div class="custom-font">
    {% assign grouped = site.publications | sort: 'date' | reverse | group_by_exp: "pub", "pub.date | date: '%Y'" %}
    {% for group in grouped %}
    <div class="mt-8 lg:flex lg:gap-1">
        <div class="lg:w-20 lg:shrink-0">
            <h2 class="!mt-0 !text-lg md:!text-xl lg:!text-xl font-bold text-stone-700 dark:text-stone-100 mb-2 lg:mb-0 border-b border-stone-200 dark:border-stone-600 pb-1 lg:border-none lg:pb-0">{{ group.name }}</h2>
        </div>
        <div class="lg:flex-1 space-y-4 md:space-y-6">
            {% for pub in group.items %}
            <div class="" key="{{ pub.id }}">
                <div class="flex flex-col space-y-0">
                    <p class="text-base md:text-lg font-bold !my-0 dark:text-stone-100">{{ pub.title }}</p>
                    <p class="text-base md:text-lg text-stone-500 dark:text-stone-300">{{ pub.authors }}</p>
                    <p class="text-[.8rem] md:text-[1rem] text-gray-400 -mt-1">
                        <span>{{ pub.venue }}</span>
                        {% for link in pub.links %}
                            <a href="{{ link.url }}" target="_blank" class="link-arrow text-sm ml-1">
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
    </div>
    {% endfor %}
</div>
