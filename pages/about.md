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
Henri Aïdasso is a Ph.D. Researcher in Computer Engineering at <a class="link" href="https://www.etsmtl.ca/en/" target="_blank">École de technologie supérieure (ÉTS)</a>, University of Quebec. His research focuses on <b>AI for Software Engineering</b>, developing data-efficient machine learning methods to improve the reliability of CI/CD pipelines and software delivery processes. This work combines <b>NLP techniques</b> for heterogeneous log analysis, <b>Language Models</b>, and <b>Statistical Methods</b> to enable intelligent automation in DevOps environments.

<br><br>
He conducts his research within the ÉTS Industrial Research Chair in DevOps (supervised by Prof. Francis Bordeleau) and as a <a class="link" href="https://www.mitacs.ca/our-programs/accelerate/">Mitacs Accelerate Fellow</a> with <a href="https://www.telus.com/en" target="_blank" class="link">TELUS</a>, where his methods are applied to production-scale distributed systems. He has been awarded the <a class="link" href="https://www.fondationarbour.com/en/bourses-d-etudes-doctoract-phd-dba/" target="_blank">Arbour Foundation Doctoral Scholarship</a> for academic excellence and leadership.

<br><br>
Parallel to his doctoral work, Henri is a part-time Applied Research Scientist at the <a class="link" href="https://crim.ca" target="_blank">Computer Research Institute of Montreal (CRIM)</a> and Lecturer at ÉTS. His broader research interests include efficient NLP for low-resource settings, NLP for Software Engineering, AI reliability, and multimodal learning.

<br><br>
Prior to his PhD, Henri was a Data Scientist at <a class="link" href="https://www.energiency.com/" target="_blank">Energiency</a> in France, where he led the development of cloud-based AI systems for real-time energy optimization in Industry 4.0 factories, designing distributed training pipelines and deploying dozens of production ML models. Earlier, he built software engineering expertise across healthcare, fintech, and public sector organizations including <a class="link" href="https://worldline.com/" target="_blank">Worldline</a> and the <a class="link" href="https://portdecotonou.bj/en/" target="_blank">Port Authority of Cotonou</a>.
</p>

<h2 class="dark:text-stone-200">Education and Honors</h2>
<p class="dark:text-stone-300">
Now in fourth year, Henri is pursing a <b>Ph.D. in Computer Engineering</b> at <a class="link" href="https://www.etsmtl.ca/en/" target="_blank">École de technologie supérieure (ÉTS)</a> in Canada, during which he has been awarded the highly selective Arbour Foundation Doctoral Scholarship. Since 2022,
he holds a <span class="font-bold">Master of Science (M.Sc.) in Big Data: Decision Support and Machine Learning</span> from the <a class="link" href="https://www.univ-rennes.fr" target="_blank">University of Rennes I</a> in France, graduating as valedictorian with the highest french academic honors, i.e. mention <i>Très Bien</i>. During his master, he gained strong theoretical foundation in machine learning and deep learning algorithms, along with advanced skills in efficiently managing and processing large-scale data.
In 2020, he earned a <b>Bachelor of Science (B.Sc.) in Computer Science</b> from the <a class="link" href="https://www.univ-rennes.fr" target="_blank">University of Rennes I</a>, also graduating as valedictorian with the highest honors.

Prior to that, he graduated top of his class in 2017 with a <b>Bachelor of Science (B.Sc.) in Computer Science and Management</b> from the <a class="link" href="https://uac.bj/" target="_blank">University of Abomey-Calavi</a> in Benin. He was then a government excellence scholar and received the trophy of excellence awarded to the best student in computer science applied to management for outstanding academic performance.
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
