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
                    <p class="text-sm md:text-base font-bold !my-0 dark:text-stone-100">
                        {{ pub.title }}
                        {% if pub.new_until %}
                            {% assign now_ts = 'now' | date: '%s' %}
                            {% assign until_ts = pub.new_until | date: '%s' %}
                            {% if now_ts < until_ts %}
                                <span class="inline-block text-xs font-semibold px-2 pt-0.5 pb-1 ml-1 rounded-full bg-green-100 text-green-700 dark:bg-green-900 dark:text-green-300 align-middle">Just accepted</span>
                            {% endif %}
                        {% endif %}
                    </p>
                    <p class="text-sm md:text-base text-stone-500 dark:text-stone-300">{{ pub.authors }}</p>
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
