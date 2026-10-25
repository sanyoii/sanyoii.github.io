(() => {
  const contents = document.querySelector('.contents');
  contents.open = window.matchMedia('(min-width: 901px)').matches;
  const bilingual = document.documentElement.dataset.bilingual === 'true';
  if (!bilingual) return;
  const button = document.getElementById('langBtn');
  function applyLanguage(lang) {
    document.documentElement.lang = lang === 'zh' ? 'zh-Hant' : 'en';
    document.querySelectorAll('[data-language]').forEach(el => {
      el.hidden = el.dataset.language !== lang;
    });
    document.querySelectorAll('[data-en][data-zh]').forEach(el => {
      el.textContent = el.dataset[lang];
    });
    document.querySelectorAll('[data-label-en]').forEach(el => {
      el.setAttribute('aria-label', lang === 'zh' ? el.dataset.labelZh : el.dataset.labelEn);
    });
    document.title = document.querySelector('h1').textContent + ' — William Lu';
    document.querySelector('meta[name="description"]').content = document.querySelector('h1').textContent + (lang === 'zh' ? ' — William Lu。本人貢獻、方法、結果與證據限制。' : ' — William Lu. My contribution, methods, outcomes, and evidence limits.');
    button.textContent = lang === 'zh' ? 'EN' : '中文';
    button.setAttribute('aria-label', lang === 'zh' ? 'Switch to English' : '切換為繁體中文');
    // Preserve section position when switching from a deep-linked heading.
    const hash = location.hash.replace(/^#(?:en|zh)-section-/, `#${lang}-section-`);
    if (hash !== location.hash) history.replaceState(null, '', hash);
  }
  let language = 'en';
  try { language = localStorage.getItem('wl-lang') === 'zh' ? 'zh' : 'en'; } catch (_) { /* English remains readable when storage is blocked. */ }
  if (/^#zh-section-/.test(location.hash)) language = 'zh';
  if (/^#en-section-/.test(location.hash)) language = 'en';
  applyLanguage(language);
  button.addEventListener('click', () => {
    language = document.documentElement.lang === 'en' ? 'zh' : 'en';
    applyLanguage(language);
    try { localStorage.setItem('wl-lang', language); } catch (_) { /* Session-only toggle. */ }
  });
})();
