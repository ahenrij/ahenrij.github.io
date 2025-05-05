---
layout: page
title: Teaching
permalink: teaching
---

<div class="custom-font">
    {% for pub in site.teachings reversed %}
    <div class="mt-4 md:mt-8" key="{{ pub.id }}">
        <div class="flex space-x-4 md:space-x-8">
            <div class="flex flex-col space-y-0">
                <p class="text-base md:text-lg font-bold !my-0 dark:text-stone-200">{{ pub.position }} - <span class="font-normal">{{ pub.term }}</span> </p>
                <p class="text-base md:text-md text-stone-500 dark:text-stone-300 ">{{ pub.course }}</p>
                <p class="text-[.9rem] md:text-[1.1rem] text-gray-400 -mt-1">{{ pub.venue }}</p>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
