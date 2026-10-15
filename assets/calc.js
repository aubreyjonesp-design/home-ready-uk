// 3-day kit and water calculator. Runs locally, stores nothing.
(function(){
  var MIN=3, COMFORT=10, DOG=1, CAT=0.25; // litres/day. MIN, COMFORT from GOV.UK Prepare.
  var f=document.getElementById('calc'), out=document.getElementById('result');
  function n(id){var v=parseInt(document.getElementById(id).value,10);return isNaN(v)||v<0?0:Math.min(v,50);}
  function c(id){return document.getElementById(id).checked;}
  function esc(s){return String(s).replace(/[&<>]/g,function(x){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[x];});}
  function r1(x){return Math.round(x*10)/10;}
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var a=n('adults'),ch=n('children'),b=n('babies'),d=n('dogs'),ca=n('cats'),days=parseInt(document.getElementById('days').value,10);
    var people=a+ch+b;
    if(people===0){out.innerHTML='<p class="note">Please enter at least one person.</p>';out.focus();return;}
    var pets=(d*DOG+ca*CAT)*days, minL=people*MIN*days+pets, comL=people*COMFORT*days+pets;
    var items=[
      'Battery or wind-up torch, plus spare batteries',
      'Battery or wind-up radio',
      'Charged power bank for each phone',
      'First aid kit (plasters, bandages, thermometer, antiseptic, gloves, tweezers)',
      'Hand sanitiser and wet wipes',
      'Food that needs no cooking for '+people+' '+(people===1?'person':'people')+' for '+days+' days (tins, crackers, nut butter, cereal bars) — buy what you normally eat',
      'Tin opener',
      'Warm layers and blankets',
      'Some cash in small notes',
      'Paper copy of key numbers (use the household plan)'];
    if(ch) items.push('Snacks, comfort items and something to do for '+ch+' '+(ch===1?'child':'children'));
    if(b) items.push('Ready-to-feed baby formula (you may not be able to boil water), nappies, wipes for '+b+' '+(b===1?'baby':'babies'));
    if(d||ca) items.push('Pet food for '+days+' days, bowls, any pet medicine, and lead or carrier');
    if(c('meds')) items.push('Enough regular medicine for several days, and a written list of names and doses');
    if(c('power')) items.push('Back-up batteries charged for medical equipment, and a paper copy of its instructions. Join the Priority Services Register');
    if(c('waterdev')) items.push('Extra water for medical equipment — ask the care team how much. Join your water company\u2019s Priority Services Register');
    if(c('mobility')) items.push('Keep kit somewhere easy to reach; spare mobility aid batteries; plan who could help you');
    if(c('sensory')) items.push('Spare hearing aid batteries or glasses; a way to get alerts (for example text or vibrating alarm); large print or audio copies of your plan');
    if(c('cognitive')) items.push('Simple picture or large-print plan; familiar comfort items; name of a trusted helper');
    if(c('older')) items.push('Arrange a neighbour or relative to check in during a power cut or cold snap. Consider the Priority Services Register');
    if(c('assist')) items.push('Food, water and waste bags for your assistance dog, and its ID');
    var h='<h2>Your checklist</h2><p><button type="button" class="noprint" onclick="window.print()">Print this checklist</button></p>';
    h+='<div class="card"><h3>Bottled water for '+days+' '+(days===1?'day':'days')+'</h3>';
    h+='<p><strong>At least '+r1(minL)+' litres</strong> (minimum for drinking).<br><strong>About '+r1(comL)+' litres</strong> to be more comfortable (cooking and washing too).</p>';
    h+='<p class="meta">Based on GOV.UK: 2.5–3 litres per person per day minimum (we use 3), 10 litres for comfort. '+(pets?'Includes about '+r1(pets)+' litres for pets (rough guide). ':'')+(b?'Babies are counted as one person each. ':'')+(c('waterdev')?'Add extra for medical equipment. ':'')+'</p>';
    h+='<p class="meta">Tip: a big pack of six 2-litre bottles holds 12 litres.</p></div>';
    h+='<div class="card"><h3>Things to keep together</h3>';
    items.forEach(function(t,i){h+='<label class="check"><input type="checkbox" id="i'+i+'"> '+esc(t)+'</label>';});
    h+='</div><p>Next: fill in your <a href="plan.html">household plan</a>. Build it up over time and eat the oldest food first, so nothing goes to waste.</p>';
    out.innerHTML=h; out.focus();
  });
})();
