---
layout: page
title: About Me
permalink: about
---

<div style="text-align: justify">

<img class="mx-auto w-1/2" src="{{site.baseurl}}/assets/img/profile.jpeg">
<p class="!py-0 !mb-0 dark:text-slate-400 text-center">I'm a nature lover.</p>
<p class="!text-gray-500 !py-0 !mt-0 !text-xs text-center">A view of the forest at Saint-Gravé, Brittany, France.</p>

<h2 class="dark:text-slate-200" style="margin-top: 24px">Summary</h2>
<p class="dark:text-slate-400">
Henri Aïdasso is a Data Scientist with two years of experience. He is currently working at <a class="text-black dark:text-slate-300" href="https://energiency.com" target="_blank">Energiency</a> using Artificial Intelligence to reduce energy consumptions in industries 4.0: timeseries forecast and systems simulation to find potential of energy savings. He has also developed several company-specific data science projects and packages within the team, including the new prediction backend for artificial intelligence models. <br>
He has a Software Engineer background, with six years of experience and has developed his skills around fullstack web/android development, DevOps practices, and cloud-based applications. He has advanced knowledge of design patterns, architecture patterns and databases.
</p>

<h2 class="dark:text-slate-200">Formation</h2>
<p class="dark:text-slate-400">
Henri will finish his Master of Science's degree in Big Data: Business Intelligence and Machine Learning in 2022 from the University of Rennes 1 in France, which he is pursuing as a work-study at Energiency.
In 2020, he graduated with a bachelor's degree in computer science from the University of Rennes 1 and finished valedictorian out of 87 students in his class. <br>
Prior to that, he worked for a year as a freelance software engineer after graduating in 2017 with a bachelor's degree in computer science applied to management from the University of Abomey-Calavi in Benin, where he was a government scholar and finished valedictorian out of 32 students.
</p>

<h2 class="dark:text-slate-200">Curriculum Vitae</h2>
	<p><a href="{{site.baseurl}}/assets/raw/202203_CV_Henri_Aidasso__en_.pdf" class="dark:text-slate-300" target="_blank">Download (2022-03)</a></p>
	<iframe 
	src="{{site.baseurl}}/assets/js/viewer/viewer.html?file={{site.baseurl}}/assets/raw/202203_CV_Henri_Aidasso__en_.pdf"
	width="100%"
	height="300px"
	style="border: none;"></iframe>

<h2 class="dark:text-slate-200">Some projects</h2>
<div>
  {% for project in site.projects %}
    <div>
		<h4><a class="!mb-0" href="{{ project.link }}" class="dark:text-slate-300" target="_blank">{{ project.title }}</a></h4>
		<p class="text-md text-gray-400 !mt-0">{{ project.description }}</p>
    </div>
  {% endfor %}
</div>

<h2 class="dark:text-slate-200">Some academic projects</h2>
<div>
  {% for project in site.academics %}
    <div>
		<h4><a class="!mb-0" href="{{ project.link }}" class="dark:text-slate-300" target="_blank">{{ project.title }}</a></h4>
		<p class="text-md text-gray-400 !mt-0">{{ project.description }}</p>
    </div>
  {% endfor %}
</div>
</div>
