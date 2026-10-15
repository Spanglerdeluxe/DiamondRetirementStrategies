(function(){
  var btn=document.getElementById('menuBtn'),nav=document.getElementById('siteNav');
  if(btn&&nav){
    var setOpen=function(o){btn.setAttribute('aria-expanded',o);nav.dataset.open=o;btn.setAttribute('aria-label',o?'Close menu':'Open menu')};
    btn.addEventListener('click',function(){setOpen(btn.getAttribute('aria-expanded')!=='true')});
    nav.addEventListener('click',function(e){if(e.target.closest('a'))setOpen(false)});
  }
  // Forms: design preview only, never submitted anywhere
  document.querySelectorAll('form[data-demo]').forEach(function(f){
    f.addEventListener('submit',function(e){
      e.preventDefault();
      var n=f.querySelector('[data-note]'),first=f.querySelector('[name="first"]');
      var name=first?first.value.trim():'';
      if(first&&!name){n.className='note';n.textContent='Add your first name so we know who to call.';first.focus();return}
      n.className='ok';
      n.textContent='Thanks'+(name?', '+name:'')+'. On the live site this request goes straight to the DRS team, who will call you within one business day.';
    });
  });
  // Copy buttons
  document.querySelectorAll('[data-copy]').forEach(function(b){
    b.addEventListener('click',function(){
      var t=b.getAttribute('data-copy');
      var done=function(){var o=b.textContent;b.textContent='Copied';setTimeout(function(){b.textContent=o},1400)};
      try{navigator.clipboard.writeText(t).then(done,function(){sel(b)})}catch(e){sel(b)}
    });
  });
  function sel(b){var s=b.previousElementSibling;if(!s)return;var r=document.createRange();r.selectNodeContents(s);var w=getSelection();w.removeAllRanges();w.addRange(r)}
  // Retirement checklist (remembered per browser)
  var cl=document.getElementById('checklist');
  if(cl){
    var boxes=[].slice.call(cl.querySelectorAll('input[type=checkbox]')),bar=document.getElementById('clBar'),txt=document.getElementById('clTxt'),KEY='drs-checklist';
    var saved={};try{saved=JSON.parse(localStorage.getItem(KEY)||'{}')}catch(e){}
    var upd=function(){var d=boxes.filter(function(b){return b.checked}).length;bar.style.width=(d/boxes.length*100)+'%';txt.textContent=d+' of '+boxes.length+' done'};
    boxes.forEach(function(b){b.checked=!!saved[b.id];b.addEventListener('change',function(){saved[b.id]=b.checked;try{localStorage.setItem(KEY,JSON.stringify(saved))}catch(e){}upd()})});
    upd();
  }
})();

(function(){
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  var header=document.querySelector('.site-header');

  /* Scroll progress + header state */
  if(header){
    var bar=document.createElement('div');bar.className='scroll-progress';header.appendChild(bar);
  }
  var ridge=document.querySelector('.hero-ridge'),gem=document.querySelector('.hero-gem'),ticking=false;
  function onScroll(){
    ticking=false;
    var y=window.scrollY,max=document.documentElement.scrollHeight-innerHeight;
    if(header){header.classList.toggle('scrolled',y>30);bar.style.setProperty('--p',max>0?Math.min(1,y/max):0)}
    if(!reduce&&y<1200){
      if(ridge)ridge.style.transform='translateY('+(y*0.12).toFixed(1)+'px)';
      if(gem)gem.style.transform='translateY('+(y*0.28).toFixed(1)+'px) rotate('+(y*0.01).toFixed(2)+'deg)';
    }
  }
  addEventListener('scroll',function(){if(!ticking){ticking=true;requestAnimationFrame(onScroll)}},{passive:true});
  onScroll();

  /* Headline words */
  var h1=document.querySelector('.hero h1');
  if(h1&&!reduce){
    var i=0;
    [].slice.call(h1.childNodes).forEach(function(n){
      if(n.nodeType===3){
        var frag=document.createDocumentFragment();
        n.textContent.split(/(\s+)/).forEach(function(part){
          if(!part)return;
          if(/^\s+$/.test(part)){frag.appendChild(document.createTextNode(part));return}
          var s=document.createElement('span');s.className='w';s.style.setProperty('--i',i++);s.textContent=part;frag.appendChild(s);
        });
        h1.replaceChild(frag,n);
      }else if(n.nodeType===1){n.classList.add('w');n.style.setProperty('--i',i++)}
    });
  }

  /* Gem light sweep */
  if(gem){
    var ns='http://www.w3.org/2000/svg';
    var defs=gem.querySelector('defs')||gem.insertBefore(document.createElementNS(ns,'defs'),gem.firstChild);
    defs.insertAdjacentHTML('beforeend','<linearGradient id="sweepG" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient><clipPath id="gemClip"><path d="M45 10h110l40 45L100 165 5 55z"/></clipPath>');
    var g=document.createElementNS(ns,'g');g.setAttribute('clip-path','url(#gemClip)');
    g.innerHTML='<rect class="gem-sweep" x="-40" y="-20" width="60" height="220" fill="url(#sweepG)" opacity=".35" transform="translate(-220 0)"/>';
    gem.appendChild(g);
  }

  /* Sparkle canvases in dark bands */
  if(!reduce){
    document.querySelectorAll('.hero, .page-hero, .cta').forEach(function(host){
      var c=document.createElement('canvas');c.className='fx-canvas';c.setAttribute('aria-hidden','true');
      var sky=host.querySelector('.hero-sky');
      if(sky)sky.after(c);else host.insertBefore(c,host.firstChild);
      sparkle(c,host.classList.contains('hero')?1:0.6);
    });
  }
  function sparkle(c,density){
    var ctx=c.getContext('2d'),w=0,h=0,dpr=Math.min(2,window.devicePixelRatio||1),stars=[],glints=[],visible=true,raf=0,t0=performance.now();
    function size(){
      var r=c.getBoundingClientRect();w=r.width;h=r.height;c.width=w*dpr;c.height=h*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);
      var n=Math.round(w*h/9000*density);stars=[];
      for(var i=0;i<n;i++)stars.push({x:Math.random()*w,y:Math.random()*h*0.75,r:Math.random()*1.2+.2,p:Math.random()*6.28,s:.6+Math.random()*1.6});
      glints=[];
      for(var j=0;j<Math.round(6*density)+2;j++)glints.push(newGlint(true));
    }
    function newGlint(any){return{x:Math.random()*w,y:any?Math.random()*h:h+10,vy:-(6+Math.random()*12),vx:(Math.random()-.5)*6,r:2+Math.random()*4.5,life:0,max:5+Math.random()*6}}
    function star4(x,y,r,a){
      ctx.save();ctx.translate(x,y);ctx.globalAlpha=a;
      var g=ctx.createRadialGradient(0,0,0,0,0,r*3);g.addColorStop(0,'rgba(230,230,255,.9)');g.addColorStop(1,'rgba(160,150,240,0)');
      ctx.fillStyle=g;ctx.beginPath();ctx.arc(0,0,r*3,0,6.283);ctx.fill();
      ctx.fillStyle='#FFFFFF';ctx.beginPath();
      ctx.moveTo(0,-r*2.2);ctx.quadraticCurveTo(0,0,r*2.2,0);ctx.quadraticCurveTo(0,0,0,r*2.2);ctx.quadraticCurveTo(0,0,-r*2.2,0);ctx.quadraticCurveTo(0,0,0,-r*2.2);ctx.fill();
      ctx.restore();
    }
    var last=performance.now();
    function frame(now){
      raf=0;if(!visible||document.hidden)return;
      var dt=Math.min(.05,(now-last)/1000),t=(now-t0)/1000;last=now;
      ctx.clearRect(0,0,w,h);
      for(var i=0;i<stars.length;i++){var s=stars[i];var a=.25+.55*(.5+.5*Math.sin(t*s.s+s.p));ctx.globalAlpha=a;ctx.fillStyle='#E4E4FA';ctx.beginPath();ctx.arc(s.x,s.y,s.r,0,6.283);ctx.fill()}
      for(var j=0;j<glints.length;j++){
        var g=glints[j];g.life+=dt;g.x+=g.vx*dt;g.y+=g.vy*dt;
        var k=g.life/g.max,al=Math.sin(Math.min(1,k)*Math.PI)*.85;
        star4(g.x,g.y,g.r*(.6+.4*Math.sin(t*3+j)),al);
        if(k>=1)glints[j]=newGlint(false),glints[j].y=Math.random()*h;
      }
      ctx.globalAlpha=1;
      raf=requestAnimationFrame(frame);
    }
    function start(){if(!raf&&visible&&!document.hidden){last=performance.now();raf=requestAnimationFrame(frame)}}
    size();start();
    var rt;addEventListener('resize',function(){clearTimeout(rt);rt=setTimeout(size,150)});
    if('IntersectionObserver' in window)new IntersectionObserver(function(e){visible=e[0].isIntersecting;start()}).observe(c);
    document.addEventListener('visibilitychange',start);
  }

  /* Services ribbon (homepage) */
  var rib=document.querySelector('.ribbon-track');
  if(rib){rib.innerHTML+=rib.innerHTML}

  /* Scroll reveal: only for things below the fold at load */
  if(!reduce&&'IntersectionObserver' in window){
    var sel='.sec-head,.intro-copy,.glance,.svc,.card,.teaser,.fig,.fear-copy,.step,.member,.estate,.flow-item,.svc-block,.split > *,.faq details,.checklist fieldset,.glossary div,.info,.form-light,.table-wrap,.strip,.cta-grid > *';
    var els=[].slice.call(document.querySelectorAll(sel));
    var io=new IntersectionObserver(function(entries){
      entries.forEach(function(e){if(e.isIntersecting){e.target.classList.remove('pre','pre-bar');io.unobserve(e.target)}});
    },{rootMargin:'0px 0px -8% 0px'});
    els.forEach(function(el){
      var r=el.getBoundingClientRect();
      el.classList.add('rv');
      if(r.top>innerHeight*0.92){
        var sib=el.parentElement?[].slice.call(el.parentElement.children).indexOf(el):0;
        el.style.setProperty('--rd',(Math.min(sib,5)*0.08)+'s');
        el.classList.add('pre');if(el.classList.contains('fig'))el.classList.add('pre-bar');
        io.observe(el);
      }
    });
    document.querySelectorAll('.step').forEach(function(s,i){s.style.setProperty('--d',i)});
  }

  /* Count-up numbers when they scroll into view */
  if(!reduce&&'IntersectionObserver' in window){
    var nums=[].slice.call(document.querySelectorAll('.fig .n, .glance dt'));
    var cio=new IntersectionObserver(function(entries){
      entries.forEach(function(e){
        if(!e.isIntersecting)return;cio.unobserve(e.target);
        var node=e.target.firstChild;if(!node||node.nodeType!==3)return;
        var m=node.textContent.match(/^(\d+)(.*)$/);if(!m)return;
        var end=+m[1],suf=m[2],st=performance.now(),dur=1400;
        (function tick(now){var k=Math.min(1,(now-st)/dur),v=Math.round(end*(1-Math.pow(1-k,3)));node.textContent=v+suf;if(k<1)requestAnimationFrame(tick)})(st);
      });
    },{threshold:.6});
    nums.forEach(function(n){cio.observe(n)});
  }

  /* Pointer spotlight + gentle tilt */
  if(!reduce&&matchMedia('(hover:hover)').matches){
    document.querySelectorAll('.svc,.card,.teaser,.fig').forEach(function(el){
      el.classList.add('tilt');
      el.addEventListener('pointermove',function(e){
        var r=el.getBoundingClientRect(),x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;
        el.style.setProperty('--mx',(x*100)+'%');el.style.setProperty('--my',(y*100)+'%');
        el.style.transform='perspective(900px) rotateX('+((.5-y)*4).toFixed(2)+'deg) rotateY('+((x-.5)*5).toFixed(2)+'deg) translateY(-4px)';
      });
      el.addEventListener('pointerleave',function(){el.style.transform=''});
    });
    /* Magnetic primary buttons */
    document.querySelectorAll('.btn-gem').forEach(function(b){
      b.addEventListener('pointermove',function(e){var r=b.getBoundingClientRect();b.style.transform='translate('+((e.clientX-r.left-r.width/2)*.15).toFixed(1)+'px,'+((e.clientY-r.top-r.height/2)*.25).toFixed(1)+'px)'});
      b.addEventListener('pointerleave',function(){b.style.transform=''});
    });
  }
})();
