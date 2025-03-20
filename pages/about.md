---
layout: page
title: About Me
permalink: about
---

<div style="text-align: justify" class="custom-font">

<img class="mx-auto !mb-0 h-56" src="{{site.baseurl}}/assets/img/nature.jpg">
<p class="!py-0 !mb-0 dark:text-slate-300">I'm a nature lover.</p>
<p class="text-gray-500 dark:text-slate-400 !py-0 !mt-0 !text-xs">A view at the <i>Old Port of Montreal</i> at Montréal, Québec, Canada.</p>

<h2 class="dark:text-stone-200 mt-32">Summary</h2>
<p class="dark:text-stone-300">
Henri Aïdasso is a Computer Engineering Ph.D. Student at <a href="https://etsmtl.ca" target="_blank">École de technologie supérieure</a>, working in the Kaloom-TELUS Industrial Research Chair in DevOps. As part of his research works, he is exploring new ways to improve DevOps processes leveraging data analytics and Artificial Intelligence: Intelligent DevOps. His work is under the supervision of Pr Francis Bordeleau.

<br>
Prior to that, he worked for two years at <a class="text-gray-500 dark:text-stone-300" href="https://www.energiency.com/" target="_blank">Energiency</a> using Artificial Intelligence to improve energy performance in industries 4.0: timeseries forecast, golden batch analysis, and digital twins modeling. He has also developed several company-specific data science projects and packages within the team, including their latest cloud-based applications stack for serving AI models. <br>
He is a Software Engineer with seven years of experience and has developed his skills around fullstack web and android development, DevOps practices, and cloud-based applications. He has advanced knowledge of design patterns, architecture patterns and databases.
</p>

<h2 class="dark:text-stone-200">Formation</h2>
<p class="dark:text-stone-300">
Since fall 2022, Henri is a doctoral student in Computer Engineering at ÉTS Montréal, University of Québec in Canada.
Just before that, he graduated top of his class with a Master of Science in Big Data: Business Intelligence and Machine Learning in 2022 from the University of Rennes 1 in France, which he completed as a work-study program at Energiency.
In 2020, he earned a Bachelor of Science in Computer Science from the University of Rennes 1 and graduated as valedictorian of his class,
one year after leaving Benin for France. <br>

Prior to that, he worked during a year as a freelance software engineer after graduating in 2017 with a bachelor's degree in Computer Science applied to Management from the University of Abomey-Calavi in Benin. He was a government scholar holder, finished valedictorian of his class, and received the trophy of excellence awarded to the best student in computer science applied to management.
</p>

<h2 class="dark:text-stone-200">Curriculum Vitae</h2>
 <p><a href="{{site.baseurl}}/assets/raw/202203_CV_Henri_Aidasso__en_.pdf" class="dark:text-stone-300" target="_blank">Download (2022-09)</a></p>
 <iframe
 src="{{site.baseurl}}/assets/js/viewer/viewer.html?file={{site.baseurl}}/assets/raw/202209_CV_Henri_Aidasso__en_.pdf"
 width="100%"
 height="300px"
 style="border: none;"></iframe>

<h2 class="dark:text-stone-200">Some projects</h2>
<div>
  {% for project in site.projects %}
    <div>
  <h4><a class="!mb-0" href="{{ project.link }}" class="dark:text-stone-300" target="_blank">{{ project.title }}</a></h4>
  <p class="text-md text-stone-500 dark:text-stone-300 !mt-0">{{ project.description }}</p>
    </div>
  {% endfor %}
</div>

<h2 class="dark:text-stone-200">Some academic projects</h2>
<div>
  {% for project in site.academics %}
    <div>
  <h4><a class="!mb-0" href="{{ project.link }}" class="dark:text-stone-300" target="_blank">{{ project.title }}</a></h4>
  <p class="text-md text-stone-500 dark:text-stone-300 !mt-0">{{ project.description }}</p>
    </div>
  {% endfor %}
</div>
</div>
