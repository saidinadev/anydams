/* ===================================
   ANYDAMS — script.js
   Modular, clean, performant
=================================== */

(function () {
  'use strict';

  /* ====== PRODUCTS DATA ====== */
  const products = [
    { name: 'Hoodie Odds', price: 'Rp 320.000', category: 'hoodie', keywords: ['hoodie', 'odds'] },
    { name: 'Jaket McLaren', price: 'Rp 580.000', category: 'jaket', keywords: ['jaket', 'mclaren', 'racing'] },
    { name: 'Pants Gradient', price: 'Rp 290.000', category: 'pants', keywords: ['pants', 'gradient', 'celana'] },
    { name: 'Cap Marlboro', price: 'Rp 120.000', category: 'topi', keywords: ['topi', 'cap', 'marlboro'] },
    { name: 'Shoes ASICS Damsik', price: 'Rp 750.000', category: 'shoes', keywords: ['shoes', 'asics', 'sneakers'] },
    { name: 'T-Shirt Guest', price: 'Rp 175.000', category: 'tshirt', keywords: ['tshirt', 'kaos', 'guest'] },
  ];

  /* ====== LOADER ====== */
  function initLoader() {
    const loader = document.getElementById('loader');
    const fill = document.getElementById('loader-fill');
    if (!loader) return;
    let progress = 0;
    const interval = setInterval(() => {
      progress += Math.random() * 15 + 5;
      if (progress >= 100) {
        progress = 100;
        clearInterval(interval);
        setTimeout(() => {
          loader.classList.add('hidden');
          document.body.style.overflow = '';
          initReveal();
          initCounters();
        }, 400);
      }
      fill.style.width = progress + '%';
    }, 80);
    document.body.style.overflow = 'hidden';
  }

  /* ====== CUSTOM CURSOR ====== */
  function initCursor() {
    const cursor = document.getElementById('cursor');
    const dot = document.getElementById('cursor-dot');
    if (!cursor || window.matchMedia('(hover:none)').matches) return;
    let mx = 0, my = 0, cx = 0, cy = 0;
    window.addEventListener('mousemove', e => { mx = e.clientX; my = e.clientY; dot.style.transform = `translate(${mx}px,${my}px) translate(-50%,-50%)`; });
    function lerp(a, b, n) { return (1 - n) * a + n * b; }
    
    const targets = document.querySelectorAll('a, button, .product-card, .tag, .faq-q, .testi-card');
    
    (function animate() {
      cx = lerp(cx, mx, 0.12); cy = lerp(cy, my, 0.12);
      
      // Magnetic effect for buttons (Only on Desktop/Hover devices)
      if (window.matchMedia('(hover:hover)').matches) {
        targets.forEach((el) => {
          if (el.classList.contains('btn-main') || el.classList.contains('nav-wa') || el.classList.contains('nav-cart-btn')) {
            const rect = el.getBoundingClientRect();
            const ex = rect.left + rect.width / 2;
            const ey = rect.top + rect.height / 2;
            const dist = Math.hypot(mx - ex, my - ey);
            if (dist < 80) {
              const pullX = (mx - ex) * 0.35;
              const pullY = (my - ey) * 0.35;
              el.style.transform = `translate(${pullX}px, ${pullY}px)`;
            } else {
              el.style.transform = '';
            }
          }
        });
      }

      cursor.style.transform = `translate(${cx}px,${cy}px) translate(-50%,-50%)`;
      requestAnimationFrame(animate);
    })();

    targets.forEach(el => {
      el.addEventListener('mouseenter', () => cursor.classList.add('hover'));
      el.addEventListener('mouseleave', () => cursor.classList.remove('hover'));
    });
    window.addEventListener('mousedown', () => cursor.classList.add('click'));
    window.addEventListener('mouseup', () => cursor.classList.remove('click'));
  }

  /* ====== NAVBAR ====== */
  function initNavbar() {
    const nav = document.getElementById('navbar');
    const links = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section[id]');
    if (!nav) return;
    window.addEventListener('scroll', () => {
      const scrollY = window.scrollY;
      nav.classList.toggle('scrolled', scrollY > 20);
      
      // Parallax
      const heroBgText = document.querySelector('.hero-bg-text');
      if (heroBgText) heroBgText.style.transform = `translateY(${scrollY * 0.25}px)`;
      
      const aboutNum = document.querySelector('.about-number');
      if (aboutNum) aboutNum.style.transform = `translateY(${scrollY * -0.05}px)`;

      // Active link
      let current = '';
      sections.forEach(s => { if (scrollY >= s.offsetTop - 100) current = s.id; });
      links.forEach(l => {
        l.classList.toggle('active', l.getAttribute('href') === '#' + current);
      });
      // BTT
      const btt = document.getElementById('btt');
      if (btt) btt.classList.toggle('on', scrollY > 600);
      // Float WA
      const fw = document.getElementById('float-wa');
      if (fw) fw.classList.toggle('visible', scrollY > 400);
    }, { passive: true });
  }

  /* ====== HAMBURGER ====== */
  function initMobileMenu() {
    const ham = document.getElementById('hamburger');
    const menu = document.getElementById('mobile-menu');
    if (!ham || !menu) return;
    ham.addEventListener('click', () => {
      ham.classList.toggle('active');
      menu.classList.toggle('open');
      document.body.style.overflow = menu.classList.contains('open') ? 'hidden' : '';
    });
    menu.querySelectorAll('.mobile-link').forEach(l => {
      l.addEventListener('click', () => {
        ham.classList.remove('active');
        menu.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  }

  /* ====== SEARCH ====== */
  function initSearch() {
    const btn = document.getElementById('search-btn');
    const overlay = document.getElementById('search-overlay');
    const closeBtn = document.getElementById('search-close');
    const input = document.getElementById('search-input');
    const results = document.getElementById('search-results');
    const tags = document.querySelectorAll('.search-tags .tag');
    if (!btn || !overlay) return;

    function open() { overlay.classList.add('open'); setTimeout(() => input && input.focus(), 100); }
    function close() { overlay.classList.remove('open'); if (input) input.value = ''; if (results) results.innerHTML = ''; }

    btn.addEventListener('click', open);
    closeBtn && closeBtn.addEventListener('click', close);
    overlay.addEventListener('click', e => { if (e.target === overlay) close(); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') close(); if (e.key === '/' && !overlay.classList.contains('open')) { e.preventDefault(); open(); } });

    tags.forEach(tag => {
      tag.addEventListener('click', () => {
        const q = tag.dataset.search || tag.textContent.toLowerCase();
        if (input) input.value = q;
        doSearch(q);
      });
    });

    let debounce;
    input && input.addEventListener('input', () => {
      clearTimeout(debounce);
      debounce = setTimeout(() => doSearch(input.value), 300);
    });

    function doSearch(q) {
      if (!results) return;
      const term = q.toLowerCase().trim();
      if (!term) { results.innerHTML = ''; return; }
      const hits = products.filter(p => p.keywords.some(k => k.includes(term)) || p.name.toLowerCase().includes(term));
      results.innerHTML = hits.length
        ? hits.map(p => `<div class="search-result-item" onclick="document.getElementById('search-close').click()"><span class="search-result-name">${p.name}</span><span class="search-result-price">${p.price}</span></div>`).join('')
        : `<div style="color:var(--muted);font-family:var(--font-mono);font-size:12px;padding:16px 0">Tidak ditemukan untuk "${q}"</div>`;
    }
  }

  // Legacy function for inline onclick compatibility
  window.triggerSearch = function(q) {
    const input = document.getElementById('search-input');
    if (input) { input.value = q; input.dispatchEvent(new Event('input')); }
  };

  /* ====== SCROLL REVEAL ====== */
  function initReveal() {
    const els = document.querySelectorAll('.reveal');
    if (!els.length) return;
    const obs = new IntersectionObserver(entries => {
      entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); obs.unobserve(e.target); } });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    els.forEach(el => obs.observe(el));
  }

  /* ====== COUNTER UP ====== */
  function initCounters() {
    const nums = document.querySelectorAll('.stat-num[data-target]');
    const obs = new IntersectionObserver(entries => {
      entries.forEach(e => {
        if (!e.isIntersecting) return;
        const el = e.target;
        const target = parseInt(el.dataset.target);
        const suffix = el.dataset.target.includes('+') ? '+' : '';
        const duration = 1400;
        const start = performance.now();
        function update(now) {
          const elapsed = now - start;
          const progress = Math.min(elapsed / duration, 1);
          const eased = 1 - Math.pow(1 - progress, 3);
          el.textContent = Math.floor(eased * target) + suffix;
          if (progress < 1) requestAnimationFrame(update);
          else el.textContent = target + suffix;
        }
        requestAnimationFrame(update);
        obs.unobserve(el);
      });
    }, { threshold: 0.5 });
    nums.forEach(n => obs.observe(n));
  }

  /* ====== PRODUCT HOVER IMAGE ====== */
  function initProductHover() {
    document.querySelectorAll('.product-card').forEach(card => {
      const mainImg = card.querySelector('.main-img');
      const hoverImgSrc = card.dataset.hoverImg;
      if (!mainImg || !hoverImgSrc) return;
      const originalSrc = mainImg.src;
      card.addEventListener('mouseenter', () => { mainImg.src = hoverImgSrc; });
      card.addEventListener('mouseleave', () => { mainImg.src = originalSrc; });
    });
  }

  /* ====== PRODUCT FILTER ====== */
  function initProductFilter() {
    const buttons = document.querySelectorAll('.filter-btn');
    const cards = document.querySelectorAll('.product-card');
    if (!buttons.length) return;
    buttons.forEach(btn => {
      btn.addEventListener('click', () => {
        buttons.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const filter = btn.dataset.filter;
        cards.forEach(card => {
          const match = filter === 'all' || card.dataset.category === filter;
          card.style.transition = 'opacity .3s, transform .3s';
          if (match) {
            card.classList.remove('hidden');
            requestAnimationFrame(() => { card.style.opacity = '1'; card.style.transform = ''; });
          } else {
            card.style.opacity = '0';
            card.style.transform = 'scale(0.95)';
            setTimeout(() => card.classList.add('hidden'), 300);
          }
        });
      });
    });
  }

  /* ====== PRODUCT MODAL ====== */
  function initModal() {
    const modal = document.getElementById('product-modal');
    const backdrop = document.getElementById('modal-backdrop');
    const closeBtn = document.getElementById('modal-close');
    if (!modal) return;

    function openModal(card) {
      const name = card.dataset.name || '';
      const price = card.dataset.price || '';
      const desc = card.dataset.desc || '';
      const img = card.dataset.img || '';
      const cat = (card.dataset.category || 'KOLEKSI').toUpperCase();
      document.getElementById('modal-title').textContent = name;
      document.getElementById('modal-price').textContent = price;
      document.getElementById('modal-desc').textContent = desc;
      document.getElementById('modal-cat').textContent = cat;
      document.getElementById('modal-img-badge').textContent = cat + ' / SS26';
      
      const modalAddBtn = document.getElementById('modal-add-cart');
      if (modalAddBtn) {
        modalAddBtn.onclick = () => {
          window.dispatchEvent(new CustomEvent('addToCart', { detail: { name, price, img } }));
          closeModal();
        };
      }

      const imgBg = document.getElementById('modal-img-bg');
      const ph = document.getElementById('modal-img-ph');
      if (img) {
        imgBg.style.background = '';
        let existing = imgBg.querySelector('img');
        if (!existing) { existing = document.createElement('img'); existing.style.cssText = 'width:100%;height:100%;object-fit:cover;object-position:top'; imgBg.insertBefore(existing, imgBg.firstChild); }
        existing.src = img; existing.alt = name;
        if (ph) ph.style.display = 'none';
      } else {
        if (ph) ph.style.display = ''; ph.textContent = name;
      }
      const waBtn = document.getElementById('modal-wa-btn');
      if (waBtn) waBtn.href = `https://wa.me/6281218216022?text=Halo%20ANYDAMS!%20Saya%20mau%20order%20${encodeURIComponent(name)}`;
      modal.classList.add('open');
      document.body.style.overflow = 'hidden';
    }

    function closeModal() { modal.classList.remove('open'); document.body.style.overflow = ''; }

    document.querySelectorAll('.btn-detail').forEach(btn => {
      btn.addEventListener('click', e => { e.stopPropagation(); openModal(btn.closest('.product-card')); });
    });
    document.querySelectorAll('.btn-add-cart').forEach(btn => {
      btn.addEventListener('click', e => {
        e.stopPropagation();
        const card = btn.closest('.product-card');
        const name = card.dataset.name || '';
        const price = card.dataset.price || '';
        const img = card.dataset.img || '';
        window.dispatchEvent(new CustomEvent('addToCart', { detail: { name, price, img } }));
      });
    });
    closeBtn && closeBtn.addEventListener('click', closeModal);
    backdrop && backdrop.addEventListener('click', closeModal);
    document.addEventListener('keydown', e => { if (e.key === 'Escape') closeModal(); });
  }

  /* ====== CART LOGIC ====== */
  function initCart() {
    let cart = JSON.parse(localStorage.getItem('anydams_cart')) || [];
    const drawer = document.getElementById('cart-drawer');
    const overlay = document.getElementById('cart-overlay');
    const btnOpen = document.getElementById('cart-btn');
    const btnClose = document.getElementById('cart-close');
    const btnCheckout = document.getElementById('btn-checkout');
    const container = document.getElementById('cart-items');
    const countBadge = document.getElementById('cart-count');
    const totalPriceEl = document.getElementById('cart-total-price');

    if (!drawer) return;

    function save() { localStorage.setItem('anydams_cart', JSON.stringify(cart)); render(); }
    function toggle(open) {
      drawer.classList.toggle('open', open);
      overlay.classList.toggle('open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    }

    function render() {
      const count = cart.reduce((acc, item) => acc + item.qty, 0);
      countBadge.textContent = count;
      countBadge.classList.toggle('visible', count > 0);

      if (cart.length === 0) {
        container.innerHTML = `<div class="cart-empty-state"><div class="cart-empty-icon">&#128722;</div><p>Keranjang kamu masih kosong.</p><button class="btn-main" id="cart-start-shopping">MULAI BELANJA</button></div>`;
        document.getElementById('cart-start-shopping')?.addEventListener('click', () => toggle(false));
        totalPriceEl.textContent = 'Rp 0';
        return;
      }

      let total = 0;
      container.innerHTML = cart.map((item, idx) => {
        const p = parseInt(item.price.replace(/\D/g, '')) || 0;
        total += p * item.qty;
        return `
          <div class="cart-item">
            <div class="cart-item-img"><img src="${item.img}" alt="${item.name}"></div>
            <div class="cart-item-info">
              <div class="cart-item-name">${item.name}</div>
              <div class="cart-item-price">${item.price}</div>
              <div class="cart-item-controls">
                <div class="qty-ctrl">
                  <button class="qty-btn" data-idx="${idx}" data-delta="-1">&#8722;</button>
                  <span class="qty-val">${item.qty}</span>
                  <button class="qty-btn" data-idx="${idx}" data-delta="1">&#43;</button>
                </div>
                <button class="cart-remove" data-idx="${idx}">Hapus</button>
              </div>
            </div>
          </div>
        `;
      }).join('');
      totalPriceEl.textContent = 'Rp ' + total.toLocaleString('id-ID');

      // Listeners inside cart
      container.querySelectorAll('.qty-btn').forEach(b => {
        b.onclick = () => {
          const idx = parseInt(b.dataset.idx);
          const delta = parseInt(b.dataset.delta);
          cart[idx].qty += delta;
          if (cart[idx].qty < 1) cart.splice(idx, 1);
          save();
        };
      });
      container.querySelectorAll('.cart-remove').forEach(b => {
        b.onclick = () => { cart.splice(parseInt(b.dataset.idx), 1); save(); };
      });
    }

    window.addEventListener('addToCart', (e) => {
      const { name, price, img } = e.detail;
      const existing = cart.find(i => i.name === name);
      if (existing) existing.qty++;
      else cart.push({ name, price, img, qty: 1 });
      save();
      toggle(true);
    });

    btnOpen?.addEventListener('click', () => toggle(true));
    btnClose?.addEventListener('click', () => toggle(false));
    overlay?.addEventListener('click', () => toggle(false));

    btnCheckout?.addEventListener('click', () => {
      if (cart.length === 0) return;
      let msg = "Halo ANYDAMS! Saya mau order koleksi berikut:\n\n";
      let total = 0;
      cart.forEach((item, i) => {
        msg += `${i+1}. ${item.name} (${item.qty}x) - ${item.price}\n`;
        total += (parseInt(item.price.replace(/\D/g, '')) || 0) * item.qty;
      });
      msg += `\nTotal: Rp ${total.toLocaleString('id-ID')}\n\nMohon info ketersediaan stok & ongkir ke alamat saya ya min. Terima kasih!`;
      window.open(`https://wa.me/6281218216022?text=${encodeURIComponent(msg)}`, '_blank');
    });

    render();
  }

  /* ====== FAQ ====== */
  function initFaq() {
    document.querySelectorAll('.faq-q').forEach(btn => {
      btn.addEventListener('click', () => {
        const item = btn.closest('.faq-item');
        const isOpen = item.classList.contains('open');
        document.querySelectorAll('.faq-item.open').forEach(i => i.classList.remove('open'));
        if (!isOpen) item.classList.add('open');
      });
    });
  }

  /* ====== NEWSLETTER ====== */
  function initNewsletter() {
    const form = document.getElementById('newsletter-form');
    if (!form) return;
    form.addEventListener('submit', e => {
      e.preventDefault();
      const input = document.getElementById('newsletter-input');
      const val = (input && input.value.trim()) || '';
      if (!val) return;
      const num = val.replace(/\D/g, '');
      if (num.length < 9) { input.style.borderColor = 'var(--accent)'; setTimeout(() => input.style.borderColor = '', 2000); return; }
      window.open(`https://wa.me/6281218216022?text=Halo%20ANYDAMS!%20Saya%20mau%20daftar%20notifikasi%20drop%20terbaru.%20No%20WA:%20${encodeURIComponent(val)}`, '_blank');
      if (input) { input.value = ''; input.placeholder = 'Terima kasih! ✓'; setTimeout(() => input.placeholder = '+62 8xx xxxx xxxx', 3000); }
    });
  }

  /* ====== SMOOTH SCROLL ====== */
  function initSmoothScroll() {
    document.querySelectorAll('a[href^="#"]').forEach(a => {
      a.addEventListener('click', e => {
        const id = a.getAttribute('href').slice(1);
        const el = document.getElementById(id);
        if (!el) return;
        e.preventDefault();
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
    });
  }

  /* ====== INIT ====== */
  function init() {
    initLoader();
    initCursor();
    initNavbar();
    initMobileMenu();
    initSearch();
    initProductFilter();
    initProductHover();
    initModal();
    initFaq();
    initNewsletter();
    initSmoothScroll();
    initCart();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
