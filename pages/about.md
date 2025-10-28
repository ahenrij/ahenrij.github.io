---
layout: page
title: About Me
permalink: about
slides:
  - image: "/assets/img/slide/oldport_montreal.jpg"
    title: "I love nature..."
    desc: "A summer view at the <i>Old Port of Montreal</i>, Montreal, Canada."
  - image: "/assets/img/slide/eclipse_montreal.jpg"
    title: "... and unique moments"
    desc: "Solar eclipse 3:27 p.m. at the <i>Saint Joseph's Oratory of Mount Royal</i>, Montreal, Canada."
  - image: "/assets/img/slide/houses_trondheim.jpg"
    title: "I find peace in beauty..."
    desc: "Colorful wooden warehouses from the <i>Gamle bybro</i>, Trondeim, Norway."
  - image: "/assets/img/slide/kanalen_trondheim.jpg"
    title: "... and beautiful landspaces"
    desc: "Morning calm on the <i>Kanalen</i> crossing the Nidelva River, Trondheim, Norway."
  - image: "/assets/img/slide/queenswharf_auckland.jpg"
    title: "... when cities breathe the sea"
    desc: "Gray afternoon at <i>Queens Wharf</i>, Auckland, New Zealand."
  - image: "/assets/img/slide/sunset_ottawa.jpg"
    title: "... and the sky whispers goodbye."
    desc: "Reddish sunset at 8:06 p.m. over the <i>Capital</i>, Ottawa, Canada."
---

<div style="text-align: justify" class="custom-font">

<div class="relative w-full max-w-3xl mx-auto overflow-hidden  h-96">
  <div id="slider" class="flex transition-transform duration-700 ease-in-out">
    {% for slide in page.slides %}
      <div class="min-w-full flex flex-col">
        <!-- Image -->
        <img class="slide-img w-full h-72 object-cover !mb-0 p-0 block"
             src="{{ site.baseurl }}{{ slide.image }}"
             alt="{{ slide.title }}"
             data-slide="{{ forloop.index0 }}">
        <!-- Caption below image -->
        <div id="caption-{{ forloop.index0 }}" 
             class="caption-box w-full px-6  text-center transition-colors duration-500">
          <p class="text-sm font-semibold text-white !-mb-3 !mt-2.5">{{ slide.title }}</p>
          <p class="text-xs text-white/90 m-0 mb-1">{{ slide.desc }}</p>
        </div>
      </div>
    {% endfor %}
  </div>

  <!-- Navigation buttons -->
  <button id="prev" 
          class="absolute top-1/2 left-4 -translate-y-1/2 bg-white/70 dark:bg-slate-800/70 hover:bg-white text-xl w-12 h-12 rounded-full flex items-center justify-center shadow-md text-slate-800 dark:text-white">
    &#10094;
  </button>

  <button id="next" 
          class="absolute top-1/2 right-4 -translate-y-1/2 bg-white/70 dark:bg-slate-800/70 hover:bg-white text-xl w-12 h-12 rounded-full flex items-center justify-center shadow-md text-slate-800 dark:text-white">
    &#10095;
  </button>
</div>

<h2 class="dark:text-stone-200 mt-32">Summary</h2>
<p class="dark:text-stone-300">
Henri Aïdasso is a Ph.D. Researcher in Engineering at <a href="https://etsmtl.ca" target="_blank">École de technologie supérieure (ÉTS)</a>, part of the University of Quebec in Canada. He works within the ÉTS Industrial Research Chair in DevOps under the supervision of Prof. Francis Bordeleau, and also as a <a href="https://www.mitacs.ca/our-programs/accelerate/">Mitacs Accelerate Fellow</a> affiliated with <a href="https://www.telus.com/en" target="_blank">TELUS</a>. His applied research focuses on optimizing the reliability of continuous integration and continuous deployment (CI/CD) pipelines in the context of highly distributed software.

This work falls under the topic of <b>Intelligent DevOps</b> and explores new ways of improving software processes using efficient Artificial Intelligence (<b>AI</b>) and Machine Learning (<b>ML</b>) techniques relying on dense and heterogeneous textual logs as well as process metrics mined from multiple software repositories.

Henri has recently been awarded the <a href="https://www.fondationarbour.com/en/bourses-d-etudes-doctoract-phd-dba/" target="_blank">Arbour Foundation Doctoral Scholarship</a> in recognition of his dedication to academic execellence, leadership, and social impact.

Beside his PhD work, he is currently a Research and Development Intern at the <a href="https://crim.ca" target="_blank">Computer Research Institute of Montreal (CRIM)</a>, where he is contributing to a range of applied AI research projects.
<br><br>
Prior to that, he worked for two years at <a class="text-gray-500 dark:text-stone-300" href="https://www.energiency.com/" target="_blank">Energiency</a> in France, leveraging ML to reduce energy consumption in large European industry 4.0 factories. In that role, he developed the cloud-based AI backend used daily for distributed training and real-time inference on dozens of customer-specific ML models. He has also developed several in-house data science Python librairies to foster best practices and reusability.

Before Energiency, Henri was a Software Engineer with 7+ years of experience across organizations in multiple domains including healthcare, education, and finance. He developed his skills around efficient backend engineering and DevOps practices. He has advanced knowledge of programming, software architecture patterns, and databases.
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

{% raw %}
<script>
  const colorThief = new ColorThief();
  const images = document.querySelectorAll('.slide-img');

  images.forEach(img => {
    if (img.complete) applyColor(img);
    else img.addEventListener('load', () => applyColor(img));
  });

  function applyColor(img) {
    try {
      const rgb = colorThief.getColor(img);
      const [r, g, b] = rgb;
      const bg = `rgba(${r}, ${g}, ${b}, 0.7)`;
      document.getElementById(`caption-${img.dataset.slide}`).style.backgroundColor = bg;
    } catch (e) {
      console.warn('Color extraction failed:', e);
    }
  }

  // Slider navigation logic
  const slider = document.getElementById('slider');
  const slides = slider.children.length;
  let index = 0;
  document.getElementById('next').onclick = () => move(1);
  document.getElementById('prev').onclick = () => move(-1);

  function move(step) {
    index = (index + step + slides) % slides;
    slider.style.transform = `translateX(-${index * 100}%)`;
  }
</script>
{% endraw %}
