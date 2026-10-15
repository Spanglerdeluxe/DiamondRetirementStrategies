/* Every page opens at the top (unless the link targets a section) */
(function(){
  try{if('scrollRestoration' in history)history.scrollRestoration='manual'}catch(e){}
  var touched=false;['wheel','touchstart','keydown','mousedown'].forEach(function(t){addEventListener(t,function(){touched=true},{once:true,passive:true})});
  function top(){if(!location.hash&&!touched)window.scrollTo(0,0)}
  top();
  addEventListener('DOMContentLoaded',top);
  addEventListener('load',function(){top();setTimeout(top,60)});
})();
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
/* Blog category filter */
(function(){
  var bar=document.querySelector('.filters');if(!bar)return;
  var cards=[].slice.call(document.querySelectorAll('.post-card')),empty=document.getElementById('noPosts');
  bar.addEventListener('click',function(e){
    var b=e.target.closest('button');if(!b)return;
    bar.querySelectorAll('button').forEach(function(x){x.setAttribute('aria-pressed',x===b)});
    var f=b.getAttribute('data-filter'),shown=0;
    cards.forEach(function(c){var on=f==='all'||c.getAttribute('data-cat')===f;c.hidden=!on;if(on)shown++;c.classList.toggle('featured',false)});
    var first=cards.find(function(c){return !c.hidden});if(first&&f==='all')first.classList.add('featured');
    if(empty)empty.hidden=shown>0;
  });
})();
