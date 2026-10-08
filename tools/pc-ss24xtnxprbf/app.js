(() => {
'use strict';
const DATA = window.COMMAND_DATA;
const CATS = DATA.categories;
const SHORT = {1:'光線',2:'拆解',3:'海報卡片',4:'商品攝影',5:'鏡頭構圖',6:'人像表情',7:'藝術畫風',8:'插畫動漫',9:'3D 材質',10:'色調',11:'場景',12:'時代復古',13:'字體排版',14:'社群版面',15:'修圖',16:'食物餐飲',17:'室內設計',18:'品牌 Logo'};
// 原文公式：主體＋場景＋風格＋光線＋鏡頭／構圖＋色調＋比例＋圖中文字
const SLOT_OF = {11:'scene',17:'scene',1:'light',5:'camera',10:'color'}; // 其餘分類歸「風格」
const SLOTS = [['scene','Scene'],['style','Style'],['light','Lighting'],['camera','Camera'],['color','Color']];
const RATIOS = {'4:5':'4:5 vertical','9:16':'9:16 vertical','16:9':'16:9 horizontal','1:1':'1:1 square'};
const TOOLS = ['ChatGPT','Gemini','Midjourney','Ideogram'];
const TEMPLATES = [ // 原文第六部分 10 組組合技
  {name:'電商商品主圖', subject:'[你的商品]', cmds:['/purewhite','/softglow','/cleanupshot'], ratio:'4:5'},
  {name:'商品情境照', subject:'[你的商品] 放在木頭桌上', cmds:['/lifestylehold','/goldenhour','/shallowdof','/filmwarm']},
  {name:'IG 輪播封面', subject:'', cmds:['/igcarousel','/bigtitle','/negspace','/warmtone'], text:'[你的標題]', ratio:'4:5'},
  {name:'YouTube 縮圖', subject:'一個驚訝的男生指著旁邊', cmds:['/ytthumb','/surprised','/pointing','/vivid','/bigtitle'], text:'[三個字]', ratio:'16:9'},
  {name:'個人品牌形象照', subject:'（上傳自己的照片）只換背景和服裝', cmds:['/keepface','/headshot','/studio','/softglow']},
  {name:'產品拆解圖', subject:'[你的產品]', cmds:['/revealparts','/techdraw','/purewhite']},
  {name:'課程文宣', subject:'', cmds:['/courseposter','/bigtitle','/speaker','/tealorange'], text:'[課程名稱]', ratio:'4:5'},
  {name:'吉祥物設計', subject:'[角色描述]', cmds:['/mascot','/cartoon3d','/charsheet'], next:'做好後再套「吉祥物・第 2 步」：同一隻角色 /consistent /expressions'},
  {name:'吉祥物・第 2 步', subject:'同一隻角色', cmds:['/consistent','/expressions'], sub:true},
  {name:'復古感生活照', subject:'[人物描述] 在街頭', cmds:['/disposable','/1990s','/grain']},
  {name:'室內設計提案圖', subject:'[坪數與空間]', cmds:['/japandi','/render3d','/daylight']},
];
const LOOK = {};
CATS.forEach(c => c.items.forEach(i => { LOOK[i.cmd] = {...i, cat:c.id}; }));
TEMPLATES.forEach(t => t.cmds.forEach(c => { if (!LOOK[c]) console.warn('template cmd missing', c); }));

const LS_FAV = 'pc.favs.v1', LS_REC = 'pc.recipes.v1';
const load = (k, d) => { try { return JSON.parse(localStorage.getItem(k)) ?? d; } catch { return d; } };
const save = (k, v) => { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} };

const st = {subject:'', sel:[], ratio:'4:5', text:'', tool:'ChatGPT', cat:1, q:'', favs:load(LS_FAV, []), recipes:load(LS_REC, [])};
const $ = id => document.getElementById(id);
const esc = s => s.replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const hasCJK = s => /[\u3400-\u9fff\uf900-\ufaff]/.test(s);

// ---------- prompt ----------
function expansions() {
  const groups = {scene:[], style:[], light:[], camera:[], color:[]};
  st.sel.forEach(c => {
    let en = LOOK[c].en;
    if (st.text.trim()) en = en.replace(/\[文字\]/g, st.text.trim());
    groups[SLOT_OF[LOOK[c].cat] || 'style'].push(en);
  });
  return groups;
}
function buildPrompt() {
  const g = expansions();
  const subj = st.subject.trim();
  const txt = st.text.trim();
  const tool = st.tool;
  if (tool === 'Midjourney') {
    const s = subj ? (hasCJK(subj) ? '[subject in English]' : subj) : '[subject in English]';
    const parts = [s, ...SLOTS.flatMap(([k]) => g[k])];
    if (txt) parts.push(`with the text "${txt}"`);
    return parts.join(', ') + ` --ar ${st.ratio}` + (txt ? '' : ' --no text');
  }
  if (tool === 'Ideogram') {
    const lines = [(subj || '[主體]') + '.'];
    SLOTS.forEach(([k, lab]) => { if (g[k].length) lines.push(`${lab}: ${g[k].join(', ')}.`); });
    lines.push(txt ? `With the text "${txt}".` : 'No text in the image.');
    lines.push(`Aspect ratio: ${RATIOS[st.ratio]}.`);
    return lines.join('\n');
  }
  // ChatGPT / Gemini：中文主體保留
  const lines = ['幫我生成一張圖：' + (subj || '[主體]')];
  SLOTS.forEach(([k, lab]) => { if (g[k].length) lines.push(`${lab}: ${g[k].join(', ')}.`); });
  lines.push(`Aspect ratio: ${RATIOS[st.ratio]}.`);
  lines.push(txt ? `Headline text: "${txt}".` : 'No text in the image.');
  return lines.join('\n');
}
const highlight = s => esc(s).replace(/\[[^\]\n]+\]/g, m => `<mark>${m}</mark>`);

function warnings() {
  const w = [], byCat = {};
  st.sel.forEach(c => (byCat[LOOK[c].cat] ||= []).push(c));
  Object.entries(byCat).forEach(([id, arr]) => {
    if (arr.length > 1) w.push({lv:'err', bad:arr, msg:`「${SHORT[id]}」選了 ${arr.length} 個（${arr.join('、')}），AI 可能二選一亂猜，建議同類只留一個。`});
  });
  if (st.sel.length > 4) w.push({lv:'warn', msg:`已選 ${st.sel.length} 個指令，超過 4 個容易互相打架，出圖四不像。`});
  if (st.tool === 'Midjourney') {
    if (hasCJK(st.subject)) w.push({lv:'info', msg:`Midjourney 看不懂中文：請把主體「${st.subject.trim().slice(0,30)}」翻成英文，替換 [subject in English]。`});
    else if (!st.subject.trim()) w.push({lv:'info', msg:'Midjourney 請用英文寫主體，替換 [subject in English]。'});
    if (hasCJK(st.text)) w.push({lv:'info', msg:'Midjourney 中文字幾乎寫不好，建議生完圖再後製加字。'});
  }
  const ph = (buildPrompt().match(/\[[^\]\n]+\]/g) || []).length;
  if (ph) w.push({lv:'info', msg:`還有 ${ph} 個黃色 [ ] 佔位，複製前記得換成你的內容。`});
  return w;
}

// ---------- render ----------
function renderTools() {
  $('tools').innerHTML = TOOLS.map(t => `<button type="button" role="radio" aria-checked="${t === st.tool}" data-tool="${t}">${t}</button>`).join('');
  $('ratios').innerHTML = Object.keys(RATIOS).map(r => `<button type="button" role="radio" aria-checked="${r === st.ratio}" data-ratio="${r}">${r}</button>`).join('');
}
function renderTemplates() {
  $('tplRow').innerHTML = '<span class="tpl-lbl">⚡ 情境模板：</span>' + TEMPLATES.map((t, i) => `<button type="button" data-tpl="${i}" title="${esc(t.cmds.join(' '))}">${esc(t.name)}</button>`).join('');
}
function renderCats() {
  const cnt = id => st.sel.filter(c => LOOK[c].cat === id).length;
  const searching = !!st.q.trim();
  $('cats').innerHTML = CATS.map(c => {
    const n = cnt(c.id);
    return `<button type="button" data-cat="${c.id}" aria-current="${!searching && st.cat === c.id}" title="${esc(c.name)}"><span>${SHORT[c.id]}</span>${n ? `<span class="dot">${n}</span>` : ''}<span class="n">${c.items.length}</span></button>`;
  }).join('') + `<hr><button type="button" data-cat="fav" aria-current="${!searching && st.cat === 'fav'}"><span>☆ 收藏</span><span class="n">${st.favs.length}</span></button>`;
}
function cardHTML(i, showCat) {
  const on = st.sel.includes(i.cmd), fav = st.favs.includes(i.cmd);
  return `<div class="card" role="button" tabindex="0" aria-pressed="${on}" data-cmd="${esc(i.cmd)}">
    ${showCat ? `<div class="cat">${esc(SHORT[LOOK[i.cmd].cat])}</div>` : ''}
    <div class="c">${esc(i.cmd)}<span class="badge">✓ 已加入</span></div>
    <div class="z">${esc(i.zh)}</div><div class="e">${highlight(i.en)}</div>
    <button type="button" class="fav" aria-pressed="${fav}" aria-label="${fav ? '取消收藏' : '收藏'} ${esc(i.cmd)}" data-fav="${esc(i.cmd)}">${fav ? '★' : '☆'}</button></div>`;
}
function renderGrid() {
  const q = st.q.trim().toLowerCase();
  let items, title, hint, showCat = false;
  if (q) {
    items = CATS.flatMap(c => c.items).filter(i => (i.cmd + ' ' + i.zh + ' ' + i.en).toLowerCase().includes(q));
    title = `搜尋「${st.q.trim()}」：${items.length} 筆`; hint = '跨 18 個分類搜尋指令名、中文效果與英文展開句。'; showCat = true;
  } else if (st.cat === 'fav') {
    items = st.favs.map(c => LOOK[c]).filter(Boolean); title = `☆ 收藏（${items.length}）`; hint = '在任一指令卡右上角點 ☆ 就會收進這裡。'; showCat = true;
  } else {
    const c = CATS.find(x => x.id === st.cat);
    items = c.items; title = `分類 ${String(c.id).padStart(2, '0')}｜${c.name}`; hint = '點卡片加入，再點一次移除。同一類建議只選一個。';
  }
  $('midTitle').textContent = title; $('midHint').textContent = hint;
  $('grid').innerHTML = items.length ? items.map(i => cardHTML(i, showCat)).join('') : `<div class="empty">${q ? '找不到符合的指令，換個關鍵字試試。' : '還沒有收藏。'}</div>`;
}
function renderSide() {
  const w = warnings();
  const bad = new Set(w.flatMap(x => x.bad || []));
  $('count').textContent = st.sel.length;
  $('chips').innerHTML = st.sel.length ? st.sel.map(c => `<span class="chip${bad.has(c) ? ' bad' : ''}" title="${esc(LOOK[c].en)}">${esc(c)} ${esc(LOOK[c].zh.split('，')[0])}<button type="button" class="x" data-remove="${esc(c)}" aria-label="移除 ${esc(c)}">✕</button></span>`).join('') : '<span class="none">還沒選指令，從左邊或中間點選。</span>';
  $('warns').innerHTML = w.map(x => `<div class="warn ${x.lv}">${x.lv === 'info' ? 'ℹ' : '⚠'} ${esc(x.msg)}</div>`).join('');
  $('toolName').textContent = st.tool;
  $('out').innerHTML = highlight(buildPrompt());
  $('recipeCount').textContent = st.recipes.length ? `(${st.recipes.length})` : '';
}
function renderAll() { renderTools(); renderCats(); renderGrid(); renderSide(); }

// ---------- actions ----------
function toggle(cmd) {
  const i = st.sel.indexOf(cmd);
  i < 0 ? st.sel.push(cmd) : st.sel.splice(i, 1);
  renderCats(); renderGrid(); renderSide();
}
let toastTimer;
function toast(msg, ms = 2200) {
  const t = $('toast'); t.textContent = msg; t.hidden = false;
  clearTimeout(toastTimer); toastTimer = setTimeout(() => { t.hidden = true; }, ms);
}
function applyTemplate(t) {
  st.subject = t.subject; st.sel = [...t.cmds]; st.text = t.text || ''; st.ratio = t.ratio || '4:5';
  $('subject').value = st.subject; $('imgText').value = st.text;
  renderAll();
  toast(`已套用「${t.name}」${t.next ? '｜' + t.next : '，把 [ ] 換成你的內容'}`, t.next ? 4500 : 2200);
}
async function copyPrompt() {
  const text = buildPrompt();
  let ok = false;
  try { if (navigator.clipboard && window.isSecureContext) { await navigator.clipboard.writeText(text); ok = true; } } catch {}
  if (!ok) {
    const ta = document.createElement('textarea');
    ta.value = text; ta.setAttribute('readonly', ''); ta.style.position = 'fixed'; ta.style.opacity = '0';
    document.body.appendChild(ta); ta.select();
    try { ok = document.execCommand('copy'); } catch { ok = false; }
    ta.remove();
  }
  const b = $('copy');
  b.textContent = ok ? '✓ 已複製' : '⚠ 複製失敗，請手動選取';
  b.classList.toggle('done', ok);
  clearTimeout(b._t); b._t = setTimeout(() => { b.textContent = '📋 一鍵複製'; b.classList.remove('done'); }, 1800);
}
function openSave() {
  $('saveRow').hidden = false;
  const n = $('recipeName');
  n.value = st.subject.trim() ? st.subject.trim().slice(0, 16) : `配方 ${st.recipes.length + 1}`;
  n.focus(); n.select();
}
function doSave() {
  const name = $('recipeName').value.trim() || `配方 ${st.recipes.length + 1}`;
  st.recipes.unshift({id: Date.now(), name, subject: st.subject, sel: [...st.sel], ratio: st.ratio, text: st.text, tool: st.tool, at: new Date().toISOString()});
  save(LS_REC, st.recipes);
  $('saveRow').hidden = true; renderSide(); toast(`已存成配方「${name}」`);
}
function renderRecipes() {
  $('recipeList').innerHTML = st.recipes.length ? st.recipes.map(r => `<div class="recipe"><div class="meta"><b>${esc(r.name)}</b><small>${esc(r.sel.join(' ') || '（沒有指令）')}｜${esc(r.ratio)}｜${esc(r.tool)}</small><small>${esc(r.subject || '（無主體）')}</small></div><button type="button" class="btn pri" data-apply="${r.id}">套用</button><button type="button" class="btn" data-del="${r.id}">刪除</button></div>`).join('') : '<p class="empty">還沒有配方。組好後按「☆ 存成配方」。</p>';
}

// ---------- events ----------
document.addEventListener('click', e => {
  const t = e.target.closest('button,[data-cmd]');
  if (!t) return;
  if (t.dataset.fav) {
    e.stopPropagation();
    const c = t.dataset.fav, i = st.favs.indexOf(c);
    i < 0 ? st.favs.push(c) : st.favs.splice(i, 1);
    save(LS_FAV, st.favs); renderCats(); renderGrid(); return;
  }
  if (t.dataset.cmd) return toggle(t.dataset.cmd);
  if (t.dataset.remove) return toggle(t.dataset.remove);
  if (t.dataset.tool) { st.tool = t.dataset.tool; renderTools(); renderSide(); return; }
  if (t.dataset.ratio) { st.ratio = t.dataset.ratio; renderTools(); renderSide(); return; }
  if (t.dataset.cat) {
    st.cat = t.dataset.cat === 'fav' ? 'fav' : +t.dataset.cat;
    st.q = ''; $('search').value = ''; $('searchClear').hidden = true;
    renderCats(); renderGrid();
    if (matchMedia('(max-width: 767.98px)').matches) window.scrollTo({top: 0});
    else document.querySelector('.mid').scrollTop = 0;
    return;
  }
  if (t.dataset.tpl) return applyTemplate(TEMPLATES[+t.dataset.tpl]);
  if (t.dataset.apply) {
    const r = st.recipes.find(x => String(x.id) === t.dataset.apply);
    if (r) { Object.assign(st, {subject: r.subject, sel: r.sel.filter(c => LOOK[c]), ratio: r.ratio, text: r.text, tool: r.tool});
      $('subject').value = st.subject; $('imgText').value = st.text; $('recipes').close(); renderAll(); toast(`已套用配方「${r.name}」`); }
    return;
  }
  if (t.dataset.del) {
    st.recipes = st.recipes.filter(x => String(x.id) !== t.dataset.del); save(LS_REC, st.recipes); renderRecipes(); renderSide(); return;
  }
});
document.addEventListener('keydown', e => {
  const c = e.target.closest && e.target.closest('[data-cmd]');
  if (c && e.target === c && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); toggle(c.dataset.cmd); }
});
$('subject').addEventListener('input', e => { st.subject = e.target.value; renderSide(); });
$('imgText').addEventListener('input', e => { st.text = e.target.value; renderSide(); });
$('search').addEventListener('input', e => { st.q = e.target.value; $('searchClear').hidden = !st.q; renderCats(); renderGrid(); });
$('searchClear').addEventListener('click', () => { st.q = ''; $('search').value = ''; $('searchClear').hidden = true; renderCats(); renderGrid(); $('search').focus(); });
$('copy').addEventListener('click', copyPrompt);
$('clearSel').addEventListener('click', () => { st.sel = []; renderCats(); renderGrid(); renderSide(); });
$('saveRecipe').addEventListener('click', openSave);
$('saveConfirm').addEventListener('click', doSave);
$('saveCancel').addEventListener('click', () => { $('saveRow').hidden = true; });
$('recipeName').addEventListener('keydown', e => { if (e.key === 'Enter') doSave(); });
$('openRecipes').addEventListener('click', () => { renderRecipes(); $('recipes').showModal(); });
$('closeRecipes').addEventListener('click', () => $('recipes').close());
const sheetToggle = () => { const open = $('side').classList.toggle('open'); $('moreBtn').textContent = open ? '收合 ▴' : '展開全文 ▾'; };
$('moreBtn').addEventListener('click', sheetToggle);
$('sheetToggle').addEventListener('click', sheetToggle);
$('sheetToggle').addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); sheetToggle(); } });

// 手機：讓清單底部留出底部列高度；分類 chips 黏在 header 下
const ro = new ResizeObserver(() => {
  const mobile = matchMedia('(max-width: 767.98px)').matches;
  document.documentElement.style.setProperty('--sheet-h', mobile ? $('side').offsetHeight + 'px' : '0px');
  document.documentElement.style.setProperty('--hdr-h', mobile ? document.querySelector('.app-header').offsetHeight + 'px' : '0px');
});
ro.observe($('side')); ro.observe(document.querySelector('.app-header'));

renderTemplates(); renderAll();
})();
