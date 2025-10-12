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
Henri Aïdasso is a Ph.D. Researcher in Computer and Software Engineering at <a href="https://etsmtl.ca" target="_blank">École de technologie supérieure (ÉTS)</a>, part of the University of Quebec in Canada. He works within the ÉTS Industrial Research Chair in DevOps under the supervision of Prof. Francis Bordeleau. As a <a href="https://www.mitacs.ca/our-programs/accelerate/">Mitacs Accelerate Fellow</a> affiliated with <a href="https://www.telus.com/en" target="_blank">TELUS</a>, his applied research focuses on optimizing the reliability of continuous integration and continuous deployment (CI/CD) pipelines in the context of highly distributed software.

This work falls under the topic of <b>Intelligent DevOps</b> and explores new ways of improving software processes using efficient Artificial Intelligence (<b>AI</b>) and Machine Learning (<b>ML</b>) techniques relying on dense and heterogeneous textual logs as well as process metrics mined from multiple software repositories.

Henri has been recently awarded the <a href="https://www.fondationarbour.com/en/bourses-d-etudes-doctoract-phd-dba/" target="_blank">Arbour Foundation Doctoral Scholarship</a> in recognition of his academic execellence, leadership, and social impact.

Beside his PhD work, he is currently a Research and Development Intern at the <a href="https://crim.ca" target="_blank">Computer Research Institute of Montreal (CRIM)</a>, where he is contributing to a range of applied research projects.
<br><br>
Prior to that, he worked for two years at <a class="text-gray-500 dark:text-stone-300" href="https://www.energiency.com/" target="_blank">Energiency</a> in France, using AI to reduce energy consumption in industry 4.0 factories. In that role, he developed a cloud-based applications stack for serving ML models, used daily for real-time training and inference on dozens of customer-specific models. He has also developed several in-house data science Python librairies to foster best practices and reusability.

Before Energiency, Henri was a Software Engineer with 7+ years of experience across organizations in multiple domains including healthcare, education, and finance. He developed his skills around efficient backend engineering and DevOps practices. He has advanced knowledge of programming, design and architecture patterns, and databases.
</p>

<h2 class="dark:text-stone-200">Education</h2>
<p class="dark:text-stone-300">
Henri is currently a Ph.D. Student in Computer and Software Engineering at <a href="https://etsmtl.ca" target="_blank">École de technologie supérieure</a> in Canada.
He hold a <span class="">Master of Science (M.Sc.) in Big Data: Decision Support and Machine Learning</span> from the <a href="https://www.univ-rennes.fr" target="_blank">University of Rennes I</a> in France (graduating top of his class with the highest honors).
In 2020, he earned a Bachelor of Science (B.Sc.) in Computer Science from the University of Rennes I, also graduating as valedictorian with highest honors.

Prior to that, he graduated top his class in 2017 with a Bachelor of Science (B.Sc.) in Computer Science applied to Management from the <a href="https://uac.bj/" target="_blank">University of Abomey-Calavi</a> in Benin. He was a government scholar and received the trophy of excellence awarded to the best student in computer science applied to management for outstanding academic performance.
</p>

<h2 class="dark:text-stone-200">Curriculum Vitae</h2>
 <p><a href="{{site.baseurl}}/assets/raw/202510_CV__en_Henri_Aidasso.pdf" class="dark:text-stone-300" target="_blank">Download (2025-10)</a></p>
 <iframe
 src="{{site.baseurl}}/assets/js/viewer/viewer.html?file={{site.baseurl}}/assets/raw/202510_CV__en_Henri_Aidasso.pdf"
 width="100%"
 height="300px"
 style="border: none;"></iframe>

<h2 class="dark:text-stone-200">Old projects</h2>
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
