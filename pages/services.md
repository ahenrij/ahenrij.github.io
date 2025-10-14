---
layout: page
title: Services
permalink: services
---

<div class="custom-font">
    {% for serv in site.services reversed %}
    <div class="mt-4 md:mt-8" key="{{ serv.id }}">
        <div class="flex space-x-4 md:space-x-8">
            <div class="text-base md:text-lg font-bold text-stone-700 dark:text-stone-100">{{ serv.year }}</div>
            <div class="flex flex-col space-y-0">
                <p class="text-base md:text-lg font-bold !my-0 dark:text-stone-100">
                    {{ serv.title }}
                    <span class="text-base md:text-lg text-stone-500 font-normal dark:text-stone-300 "> for the {{ serv.venue }}</span>
                    <a href="{{ serv.link }}" target="_blank" class="inline-flex items-center text-base mr-2 pl-2 !no-underline hover:!underline">
                        website
                        {% include arrow-ne.html %}
                    </a>
                </p>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
