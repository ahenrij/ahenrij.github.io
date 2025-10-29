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

<div class="w-full max-w-3xl mx-auto overflow-hidden">
  <!-- Slider wrapper -->
  <div id="slider" class="flex transition-transform duration-700 ease-in-out">
    {% for slide in page.slides %}
      <div class="min-w-full flex flex-col">
        <!-- Image -->
        <img class="slide-img w-full h-72 md:h-80 object-cover !mb-0 block"
          src="{{ site.baseurl }}{{ slide.image }}"
          alt="{{ slide.title }}"
          data-slide="{{ forloop.index0 }}">
        <!-- Caption block -->
        <div id="caption-{{ forloop.index0 }}" 
          class="caption-box w-full px-6 py-0 text-center transition-colors duration-500">
          <p class="text-sm font-semibold !mb-0 !mt-0 pt-3 text-white">{{ slide.title }}</p>
          <p class="text-xs text-white/90 !mt-0 !mb-0 pt-1 !pb-4">{{ slide.desc }}</p>
        </div>
      </div>
    {% endfor %}
  </div>

  <!-- Navigation buttons -->
  <div class="flex justify-between items-center w-full mt-4 px-2">
    <button 
      id="prev"
      class="text-lg font-semibold text-slate-800 dark:text-white hover:underline transition"
    >← Prev</button>
    <button 
      id="next"
      class="text-lg font-semibold text-slate-800 dark:text-white hover:underline transition"
    >Next →</button>
  </div>
</div>


<h2 class="dark:text-stone-200 mt-32">Summary</h2>
<p class="dark:text-stone-300">
Henri Aïdasso is a Ph.D. Researcher in Computer Engineering at <a class="link" href="https://etsmtl.ca" target="_blank">École de technologie supérieure (ÉTS)</a>, University of Quebec in Canada. He works as part of the ÉTS Industrial Research Chair in DevOps under the supervision of Prof. Francis Bordeleau, focusing on analytics and AI-powered measurement and improvement of software process quality. He is also a <a class="link" href="https://www.mitacs.ca/our-programs/accelerate/">Mitacs Accelerate Fellow</a> affiliated with <a href="https://www.telus.com/en" target="_blank" class="link">TELUS</a>, where he conducts applied AI research to improve the efficiency and reliability of CI/CD pipelines.

<br><br>
His PhD work falls under the topic of Intelligent DevOps research, aimed at finding new ways of improving software processes using efficient <b>Artificial Intelligence (AI)</b> and <b>Machine Learning (ML)</b> algorithms. As such, Henri has developed expertise in <b>NLP techniques</b> for collecting, processing, and representing dense and heterogeneous textual logs, as well as in applying <b>Language Models</b>, ML models, and <b>Statistical Analysis</b> to derive insights from process metrics and enable intelligent automation.

Henri has been awarded the prestigious <a class="link" href="https://www.fondationarbour.com/en/bourses-d-etudes-doctoract-phd-dba/" target="_blank">Arbour Foundation Doctoral Scholarship</a> in recognition of his continued academic execellence, leadership, and social impact.

<br><br>
Beside his PhD work, Henri is a part-time Lecturer at the École de technologie supérieure (ÉTS) and a Research and Development Intern at the <a class="link" href="https://crim.ca" target="_blank">Computer Research Institute of Montreal (CRIM)</a>, where he contributes to a range of applied AI research projects. In his spare time, he explores innovative approaches to make NLP more efficient in low-resource settings.

<br><br>
Prior to that, he was a Data Scientist at <a class="link" href="https://www.energiency.com/" target="_blank">Energiency</a> in France, where he leveraged ML and Deep Learning to reduce energy consumption in large European industry 4.0 factories. In that role, he led multiple ML Engineering projects, developing the cloud-based AI backend for distributed training and real-time inference workflows for dozens of customer-specific models used daily in production. He has also developed several in-house data science Python librairies to foster best practices and reusability.

<br><br>
Before joining Energiency, he built a strong foundation in software engineering, accumulating over seven years of experience across the healthcare, education, and finance sectors across organizations such as <a class="link" href="https://worldline.com/" target="_blank">Worldline</a> and the <a class="link" href="https://portdecotonou.bj/en/" target="_blank">Port Authority of Cotonou</a>. He developed strong skills in efficient backend engineering and DevOps, along with advanced programming, architecture patterns, and database systems, which he now leverages in his fundamental and applied AI research works.
</p>

<h2 class="dark:text-stone-200">Education</h2>
<p class="dark:text-stone-300">
Now in fourth year, Henri is pursing a <b>Ph.D. in Computer Engineering</b> at <a class="link" href="https://etsmtl.ca" target="_blank">École de technologie supérieure (ÉTS)</a> in Canada.
He holds a <span class="font-bold">Master of Science (M.Sc.) in Big Data: Decision Support and Machine Learning</span> from the <a class="link" href="https://www.univ-rennes.fr" target="_blank">University of Rennes I</a> in France (graduating in 2022, top of his class with the highest honors), where he gained strong theoretical foundation in machine learning and deep learning algorithms, along with advanced skills in efficiently managing and processing large-scale data.
In 2020, he earned a <b>Bachelor of Science (B.Sc.) in Computer Science</b> from the University of Rennes I, also graduating as valedictorian with highest honors.

Prior to that, he graduated top his class in 2017 with a <b>Bachelor of Science (B.Sc.) in Computer Science and Management</b> from the <a class="link" href="https://uac.bj/" target="_blank">University of Abomey-Calavi</a> in Benin. He was a government scholar and received the trophy of excellence awarded to the best student in computer science applied to management for outstanding academic performance.
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
