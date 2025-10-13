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
                            <svg xmlns="http://www.w3.org/2000/svg" width="8" height="8" viewBox="0 0 10 10" class="ml-1 mt-1">
                                <path d="M7.849,15.54,14.76,8.629v2.988a.833.833,0,0,0,1.667,0v-5a.832.832,0,0,0-.833-.833h-5a.833.833,0,1,0,0,1.667h2.988L6.671,14.362A.833.833,0,0,0,7.849,15.54Z" transform="translate(-6.427 -5.784)" fill="currentColor"/>
                            </svg>
                        </a>
                        {% unless forloop.last %} {% endunless %}
                    {% endfor %}
                </p>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
