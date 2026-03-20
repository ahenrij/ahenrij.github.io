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
    title: "... in beautiful landspaces"
    desc: "Morning calm on the <i>Kanalen</i> crossing the Nidelva River, Trondheim, Norway."
  - image: "/assets/img/slide/queenswharf_auckland.jpg"
    title: "... when cities breathe the sea"
    desc: "Gray afternoon at <i>Queens Wharf</i>, Auckland, New Zealand."
  - image: "/assets/img/slide/sunset_ottawa.jpg"
    title: "... and the sky whispers goodbye."
    desc: "Reddish sunset at 8:06 p.m. over the <i>Capital</i>, Ottawa, Canada."
---

<div style="text-align: justify; margin-top: -1rem;" class="custom-font">

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

<h2 class="dark:text-stone-200 mt-12">Background</h2>
<p class="dark:text-stone-300">
Henri Aïdasso is a Ph.D. Researcher in Computer Engineering at <a class="link" href="https://www.etsmtl.ca/en/" target="_blank">École de technologie supérieure (ÉTS)</a>, University of Quebec, working within the ÉTS Industrial Research Chair in DevOps (Prof. Francis Bordeleau) and as a <a class="link" href="https://www.mitacs.ca/our-programs/accelerate/">Mitacs Accelerate Fellow</a> with <a class="link" href="https://www.telus.com/en" target="_blank">TELUS</a>. His research focuses on <b>AI for Software Engineering</b>, applying Machine Learning, NLP, and Language Models to execution logs and process metrics for intelligent reliability engineering in CI/CD systems. Parallel to his doctoral work, he is a part-time Research & Development Intern at <a class="link" href="https://crim.ca" target="_blank">CRIM</a> and a part-time Lecturer at ÉTS. Prior to his PhD, he was a Data Scientist at <a class="link" href="https://www.energiency.com/" target="_blank">Energiency</a> (France), leading the engineering of ML systems for real-time energy optimization in Industry 4.0, and earlier built software engineering expertise across a variety of organizations including <a class="link" href="https://worldline.com/" target="_blank">Worldline</a> and the <a class="link" href="https://portdecotonou.bj/" target="_blank">Port Authority of Cotonou</a>.
</p>

<h2 class="dark:text-stone-200">Education</h2>

<div class="not-prose mt-4 relative border-l-2 border-stone-200 dark:border-dark-border ml-2 space-y-6 pb-2">

  <div class="relative pl-6">
    <div class="absolute -left-1.5 top-[0.35rem] w-3 h-3 rounded-full bg-emerald-600 dark:bg-dark-accent border-2 border-white dark:border-dark-bg"></div>
    <span class="text-xs font-mono text-stone-400 dark:text-stone-500">2022 – present</span>
    <p class="font-bold text-sm md:text-base dark:text-stone-100 mt-0.5 mb-0">Ph.D. in Computer Engineering</p>
    <p class="text-sm text-stone-500 dark:text-stone-400 mt-0 mb-0"><a class="link" href="https://www.etsmtl.ca/en/" target="_blank">École de technologie supérieure (ÉTS)</a>, University of Quebec, Canada</p>
    <p class="text-xs text-stone-400 dark:text-stone-500 mt-1 mb-0">Mitacs Accelerate Fellow (TELUS) · Arbour Foundation Scholar</p>
  </div>

  <div class="relative pl-6">
    <div class="absolute -left-1.5 top-[0.35rem] w-3 h-3 rounded-full bg-stone-300 dark:bg-dark-elevated border-2 border-white dark:border-dark-bg"></div>
    <span class="text-xs font-mono text-stone-400 dark:text-stone-500">2020 – 2022</span>
    <p class="font-bold text-sm md:text-base dark:text-stone-100 mt-0.5 mb-0">M.Sc. in Big Data: Analytics and Learning</p>
    <p class="text-sm text-stone-500 dark:text-stone-400 mt-0 mb-0"><a class="link" href="https://www.univ-rennes.fr" target="_blank">University of Rennes</a>, France</p>
    <p class="text-xs text-stone-400 dark:text-stone-500 mt-1 mb-0">Valedictorian · Highest Honors (Mention Très Bien)</p>
  </div>

  <div class="relative pl-6">
    <div class="absolute -left-1.5 top-[0.35rem] w-3 h-3 rounded-full bg-stone-300 dark:bg-dark-elevated border-2 border-white dark:border-dark-bg"></div>
    <span class="text-xs font-mono text-stone-400 dark:text-stone-500">2019 – 2020</span>
    <p class="font-bold text-sm md:text-base dark:text-stone-100 mt-0.5 mb-0">B.Sc. in Computer Science</p>
    <p class="text-sm text-stone-500 dark:text-stone-400 mt-0 mb-0"><a class="link" href="https://www.univ-rennes.fr" target="_blank">University of Rennes</a>, France</p>
    <p class="text-xs text-stone-400 dark:text-stone-500 mt-1 mb-0">Valedictorian · Highest Honors (Mention Très Bien)</p>
  </div>

  <div class="relative pl-6">
    <div class="absolute -left-1.5 top-[0.35rem] w-3 h-3 rounded-full bg-stone-300 dark:bg-dark-elevated border-2 border-white dark:border-dark-bg"></div>
    <span class="text-xs font-mono text-stone-400 dark:text-stone-500">2014 – 2017</span>
    <p class="font-bold text-sm md:text-base dark:text-stone-100 mt-0.5 mb-0">B.Sc. in Computer Science and Management</p>
    <p class="text-sm text-stone-500 dark:text-stone-400 mt-0 mb-0"><a class="link" href="https://uac.bj/" target="_blank">University of Abomey-Calavi</a>, Benin</p>
    <p class="text-xs text-stone-400 dark:text-stone-500 mt-1 mb-0">Government Excellence Scholar</p>
  </div>

</div>

<h2 class="dark:text-stone-200">Awards & Recognition</h2>

<div class="not-prose grid grid-cols-1 md:grid-cols-2 gap-3 mt-4">

  <div class="theme-card rounded-lg p-4 flex gap-3 items-start">
    <i class="fas fa-award text-emerald-600 dark:text-dark-accent mt-0.5 text-base shrink-0"></i>
    <div>
      <p class="font-semibold text-sm dark:text-stone-100 leading-snug mb-0"><a class="link" href="https://www.fondationarbour.com/en/bourses-d-etudes-doctoract-phd-dba/" target="_blank">Arbour Foundation Doctoral Scholarship</a></p>
      <p class="text-xs text-stone-500 dark:text-stone-400 mt-1 mb-0">Academic excellence and leadership · $30,000 CAD · 2025</p>
    </div>
  </div>

  <div class="theme-card rounded-lg p-4 flex gap-3 items-start">
    <i class="fas fa-flask text-emerald-600 dark:text-dark-accent mt-0.5 text-base shrink-0"></i>
    <div>
      <p class="font-semibold text-sm dark:text-stone-100 leading-snug mb-0"><a class="link" href="https://www.mitacs.ca/our-programs/accelerate/" target="_blank">Mitacs Accelerate Fellowship</a></p>
      <p class="text-xs text-stone-500 dark:text-stone-400 mt-1 mb-0">Industry-academic research partnership with TELUS · $72,000 CAD over 3 years · 2023</p>
    </div>
  </div>

  <div class="theme-card rounded-lg p-4 flex gap-3 items-start">
    <i class="fas fa-graduation-cap text-emerald-600 dark:text-dark-accent mt-0.5 text-base shrink-0"></i>
    <div>
      <p class="font-semibold text-sm dark:text-stone-100 leading-snug mb-0">Valedictorian, M.Sc. in Big Data &amp; ML</p>
      <p class="text-xs text-stone-500 dark:text-stone-400 mt-1 mb-0">Highest Honors (Mention Très Bien) · University of Rennes · 2022</p>
    </div>
  </div>

  <div class="theme-card rounded-lg p-4 flex gap-3 items-start">
    <i class="fas fa-graduation-cap text-emerald-600 dark:text-dark-accent mt-0.5 text-base shrink-0"></i>
    <div>
      <p class="font-semibold text-sm dark:text-stone-100 leading-snug mb-0">Valedictorian, B.Sc. in CS</p>
      <p class="text-xs text-stone-500 dark:text-stone-400 mt-1 mb-0">Highest Honors (Mention Très Bien) · University of Rennes · 2020</p>
    </div>
  </div>

  <div class="theme-card rounded-lg p-4 flex gap-3 items-start">
    <i class="fas fa-graduation-cap text-emerald-600 dark:text-dark-accent mt-0.5 text-base shrink-0"></i>
    <div>
      <p class="font-semibold text-sm dark:text-stone-100 leading-snug mb-0">Valedictorian &amp; Trophy of Excellence, B.Sc. in CS &amp; Management</p>
      <p class="text-xs text-stone-500 dark:text-stone-400 mt-1 mb-0">University of Abomey-Calavi · 2017</p>
    </div>
  </div>

  <div class="theme-card rounded-lg p-4 flex gap-3 items-start">
    <i class="fas fa-star text-emerald-600 dark:text-dark-accent mt-0.5 text-base shrink-0"></i>
    <div>
      <p class="font-semibold text-sm dark:text-stone-100 leading-snug mb-0">Government Excellence Scholarship</p>
      <p class="text-xs text-stone-500 dark:text-stone-400 mt-1 mb-0">Free tuition + 1,200,000 XOF over 3 years · University of Abomey-Calavi · 2014</p>
    </div>
  </div>

</div>

<h2 class="dark:text-stone-200">Curriculum Vitae</h2>
 <p><a href="{{site.baseurl}}/assets/raw/CV_Henri_Aidasso.pdf" class="link" target="_blank">Download (2026)</a></p>
 <iframe
 src="{{site.baseurl}}/assets/js/viewer/viewer.html?file={{site.baseurl}}/assets/raw/CV_Henri_Aidasso.pdf"
 width="100%"
 height="300px"
 style="border: none;"></iframe>


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
