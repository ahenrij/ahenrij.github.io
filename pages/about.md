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
Henri J. Aïdasso is an Engineering Ph.D. Student at <a href="https://etsmtl.ca" target="_blank">École de technologie supérieure</a> in Canada, working in the Kaloom-TELUS Industrial Research Chair in DevOps under the supervision of Prof. Francis Bordeleau. As part of his research works, he is exploring Intelligent DevOps approaches, i.e. new ways to improve DevOps processes using Artificial Intelligence (AI) and heterogeneous - textual logs and tabular - data available in software repositories. He is also a Mitacs Accelerate Fellow, working at <a href="https://www.telus.com/en/blog/business/what-is-a-software-defined-wide-area-network-sd-wan" target="_blank">TELUS</a> on its network softwarisation DevOps processes.

Prior to that, he worked for two years at <a class="text-gray-500 dark:text-stone-300" href="https://www.energiency.com/" target="_blank">Energiency</a> in France, using AI to reduce energy consumption in industry 4.0 factories. In that role, he developed a cloud-based applications stack for deploying ML models, used daily for real-time training and predictions of dozens models across the teams. He has also developed several company-specific data science librairies to foster best practices and reusability.

Before Energiency, Henri was a Software Engineer with 6+ years of experience across organizations in multiple domains including healthcare, education, and finance. He developed his skills around fullstack web and mobile development and DevOps practices. He has advanced knowledge of design patterns, architecture patterns, and databases.
</p>

<h2 class="dark:text-stone-200">Formation</h2>
<p class="dark:text-stone-300">
Henri is currently a Ph.D. Student in Computer Engineering at <a href="https://etsmtl.ca" target="_blank">École de technologie supérieure</a> in Canada.
He hold (graduating top of his class in 2022) a Master of Science in Big Data: Business Intelligence and Machine Learning from the University of Rennes 1 in France.
In 2020, he earned a Bachelor of Science in Computer Science from the University of Rennes 1, also graduating as valedictorian.

Prior to that, he graduated top his class in 2017 with a Bachelor of Science in Computer Science applied to Management from the University of Abomey-Calavi in Benin. He was a government scholar holder, and received the trophy of excellence awarded to the best student in computer science applied to management.
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

<h2 class="dark:text-stone-200 hidden">Some academic projects</h2>
<div class="hidden">
  {% for project in site.academics %}
    <div>
  <h4><a class="!mb-0" href="{{ project.link }}" class="dark:text-stone-300" target="_blank">{{ project.title }}</a></h4>
  <p class="text-md text-stone-500 dark:text-stone-300 !mt-0">{{ project.description }}</p>
    </div>
  {% endfor %}
</div>
</div>
