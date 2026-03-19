html = """<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>ANYDAMS — Anything Damsik</title>
  <meta name="description" content="ANYDAMS adalah brand streetwear lokal Jakarta. Original design, limited drops, authentic culture."/>
  <meta property="og:title" content="ANYDAMS — Anything Damsik"/>
  <meta property="og:description" content="Streetwear Jakarta. Bukan ikut-ikutan, bukan setengah-setengah."/>
  <meta property="og:image" content="ootd.jpg"/>
  <meta name="theme-color" content="#080808"/>
  <link rel="preconnect" href="https://fonts.googleapis.com"/>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
  <link href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@300;400;500;600;700;800;900&family=Barlow:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet"/>
  <link rel="stylesheet" href="style.css"/>
</head>
<body>

<div class="cursor" id="cursor"></div>
<div class="cursor-dot" id="cursor-dot"></div>

<div class="loader" id="loader">
  <div class="loader-inner">
    <div class="loader-logo">AD</div>
    <div class="loader-bar"><div class="loader-fill" id="loader-fill"></div></div>
    <div class="loader-text">LOADING COLLECTION</div>
  </div>
</div>

<nav id="navbar">
  <div class="nav-left"><a href="#beranda" class="nav-logo">ANYDAMS</a></div>
  <div class="nav-center">
    <a href="#beranda" class="nav-link active">Home</a>
    <a href="#tentang" class="nav-link">About</a>
    <a href="#koleksi" class="nav-link">Koleksi</a>
    <a href="#lookbook" class="nav-link">Lookbook</a>
    <a href="#info" class="nav-link">Info</a>
  </div>
  <div class="nav-right">
    <button class="nav-search-btn" id="search-btn" aria-label="Search">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="m21 21-4.35-4.35"/></svg>
    </button>
    <a href="https://wa.me/6281218216022" target="_blank" class="nav-wa">
      <svg width="13" height="13" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>
      Order WA
    </a>
    <button class="hamburger" id="hamburger" aria-label="Menu"><span></span><span></span></button>
  </div>
</nav>

<div class="search-overlay" id="search-overlay">
  <div class="search-overlay-inner">
    <button class="search-close" id="search-close">&#x2715;</button>
    <div class="search-label">CARI PRODUK</div>
    <input type="text" class="search-input" id="search-input" placeholder="ketik nama produk..." autocomplete="off"/>
    <div class="search-results" id="search-results"></div>
    <div class="search-tags">
      <span class="tag" onclick="triggerSearch('hoodie')">Hoodie</span>
      <span class="tag" onclick="triggerSearch('pants')">Pants</span>
      <span class="tag" onclick="triggerSearch('jaket')">Jaket</span>
      <span class="tag" onclick="triggerSearch('topi')">Cap</span>
      <span class="tag" onclick="triggerSearch('shoes')">Sneakers</span>
      <span class="tag" onclick="triggerSearch('tshirt')">T-Shirt</span>
    </div>
  </div>
</div>

<div class="mobile-menu" id="mobile-menu">
  <div class="mobile-menu-inner">
    <a href="#beranda" class="mobile-link" data-num="01">Home</a>
    <a href="#tentang" class="mobile-link" data-num="02">About</a>
    <a href="#koleksi" class="mobile-link" data-num="03">Koleksi</a>
    <a href="#lookbook" class="mobile-link" data-num="04">Lookbook</a>
    <a href="#info" class="mobile-link" data-num="05">Info</a>
    <a href="https://wa.me/6281218216022" class="mobile-link mobile-wa" target="_blank" data-num="&#x2192;">WhatsApp Order</a>
  </div>
  <div class="mobile-menu-foot">
    <span>ANYDAMS &#169; 2026</span>
    <div class="mobile-socials">
      <a href="https://instagram.com/anydams.id" target="_blank">IG</a>
      <a href="https://tiktok.com/@anydams.id" target="_blank">TT</a>
    </div>
  </div>
</div>

<!-- HERO -->
<section id="beranda" class="hero">
  <div class="hero-bg-text">ANYDAMS</div>
  <div class="hero-content">
    <div class="hero-left">
      <div class="hero-tag reveal">
        <span class="tag-dot"></span>
        <span>SS26 &mdash; Jakarta, Indonesia</span>
      </div>
      <h1 class="hero-title reveal delay-1">
        <span class="hero-line">ANY</span>
        <span class="hero-line italic">
          <span class="word-rotator">
            <span class="word-rotator-inner">
              <span>DAMS.</span>
              <span>AUTHENTIC.</span>
              <span>ORIGINAL.</span>
            </span>
          </span>
        </span>
      </h1>
      <p class="hero-sub reveal delay-2">Streetwear yang dibuat berbeda.<br>Bukan ikut-ikutan, bukan setengah-setengah.</p>
      <div class="hero-actions reveal delay-3">
        <a href="#koleksi" class="btn-main">Lihat Koleksi <span class="arrow">&#x2192;</span></a>
        <a href="#tentang" class="btn-line">Our Story</a>
      </div>
    </div>
    <div class="hero-right">
      <div class="hero-img-frame">
        <div class="hero-img-label">OOTD / SS26</div>
        <img src="ootd.jpg" alt="ANYDAMS OOTD SS26" class="hero-img"/>
        <div class="hero-img-badge">
          <div class="badge-line">LIMITED</div>
          <div class="badge-line accent">DROP SS26</div>
        </div>
      </div>
    </div>
  </div>
  <div class="hero-scroll-line">
    <span class="scroll-text">SCROLL</span>
    <div class="scroll-bar"><div class="scroll-bar-fill"></div></div>
  </div>
</section>

<!-- MARQUEE -->
<div class="marquee-section">
  <div class="marquee-wrap">
    <div class="marquee-track">
      <span>ANYDAMS</span><span class="dot">&#9679;</span>
      <span>STREETWEAR JAKARTA</span><span class="dot">&#9679;</span>
      <span class="red">LIMITED EDITION</span><span class="dot">&#9679;</span>
      <span>ANYTHING DAMSIK</span><span class="dot">&#9679;</span>
      <span>ORIGINAL DESIGN</span><span class="dot">&#9679;</span>
      <span>SS26 COLLECTION</span><span class="dot">&#9679;</span>
      <span>ANYDAMS</span><span class="dot">&#9679;</span>
      <span>STREETWEAR JAKARTA</span><span class="dot">&#9679;</span>
      <span class="red">LIMITED EDITION</span><span class="dot">&#9679;</span>
      <span>ANYTHING DAMSIK</span><span class="dot">&#9679;</span>
      <span>ORIGINAL DESIGN</span><span class="dot">&#9679;</span>
      <span>SS26 COLLECTION</span><span class="dot">&#9679;</span>
    </div>
  </div>
  <div class="marquee-wrap reverse">
    <div class="marquee-track">
      <span>AUTHENTIC</span><span class="dot">&#9679;</span>
      <span class="red">BUKAN KEMBAR</span><span class="dot">&#9679;</span>
      <span>HANDMADE</span><span class="dot">&#9679;</span>
      <span>LOKAL ASLI</span><span class="dot">&#9679;</span>
      <span>DAMSIK VIBES</span><span class="dot">&#9679;</span>
      <span>AUTHENTIC</span><span class="dot">&#9679;</span>
      <span class="red">BUKAN KEMBAR</span><span class="dot">&#9679;</span>
      <span>HANDMADE</span><span class="dot">&#9679;</span>
      <span>LOKAL ASLI</span><span class="dot">&#9679;</span>
      <span>DAMSIK VIBES</span><span class="dot">&#9679;</span>
    </div>
  </div>
</div>

<!-- ABOUT -->
<section id="tentang" class="about">
  <div class="about-grid">
    <div class="about-media reveal">
      <div class="about-number">01</div>
      <div class="about-img-block">
        <img src="images/hoodie-odds.jpg" alt="ANYDAMS Hoodie" loading="lazy"/>
        <div class="about-img-overlay"><span>SS26 / HOODIE ODDS</span></div>
      </div>
      <div class="about-stat-cards">
        <div class="stat-card">
          <div class="stat-num" data-target="500">0</div>
          <div class="stat-label">Pieces Sold</div>
        </div>
        <div class="stat-card accent-card">
          <div class="stat-num" data-target="12">0</div>
          <div class="stat-label">Collections</div>
        </div>
        <div class="stat-card">
          <div class="stat-num" data-target="100">0</div>
          <div class="stat-label">% Original</div>
        </div>
      </div>
    </div>
    <div class="about-right reveal delay-2">
      <div class="section-eyebrow">Tentang Kami</div>
      <h2 class="section-title">Bukan Sekadar<br>Brand <span class="thin">Biasa</span></h2>
      <div class="about-divider"></div>
      <p class="about-body">ANYDAMS lahir dari jalanan Jakarta — dari kultur yang hidup, bukan yang dibuat-buat. Kami percaya bahwa pakaian adalah ekspresi, bukan seragam.</p>
      <p class="about-body">Setiap piece dirancang dengan tangan, dengan cerita, dengan tujuan. Limited. Authentic. Damsik.</p>
      <div class="about-values">
        <div class="value-item">
          <span class="value-icon">&#9670;</span>
          <div>
            <div class="value-title">LIMITED DROPS</div>
            <div class="value-desc">Setiap koleksi dibuat terbatas. Kalau kehabisan, ya kehabisan.</div>
          </div>
        </div>
        <div class="value-item">
          <span class="value-icon">&#9670;</span>
          <div>
            <div class="value-title">ORIGINAL DESIGN</div>
            <div class="value-desc">Semua desain original dari tim ANYDAMS. Tidak ada tiruan.</div>
          </div>
        </div>
        <div class="value-item">
          <span class="value-icon">&#9670;</span>
          <div>
            <div class="value-title">QUALITY FIRST</div>
            <div class="value-desc">Material premium, jahitan kuat, layak dipakai bertahun-tahun.</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- STATEMENT -->
<div class="statement-banner">
  <div class="statement-inner reveal">
    <div class="statement-quote">&ldquo;</div>
    <p class="statement-text">Kenakan sesuatu yang<br><em>mencerminkan siapa kamu</em>,<br>bukan siapa orang lain.</p>
  </div>
</div>

<!-- KOLEKSI -->
<section id="koleksi" class="koleksi">
  <div class="koleksi-head">
    <div>
      <div class="section-eyebrow">Koleksi</div>
      <h2 class="section-title">Drop <span class="thin">SS26</span></h2>
    </div>
    <div class="koleksi-head-right">
      <div class="filter-tabs">
        <button class="filter-btn active" data-filter="all">ALL</button>
        <button class="filter-btn" data-filter="hoodie">HOODIE</button>
        <button class="filter-btn" data-filter="pants">PANTS</button>
        <button class="filter-btn" data-filter="jaket">JAKET</button>
        <button class="filter-btn" data-filter="topi">CAP</button>
        <button class="filter-btn" data-filter="shoes">SHOES</button>
        <button class="filter-btn" data-filter="tshirt">TSHIRT</button>
      </div>
    </div>
  </div>
  <div class="product-grid" id="product-grid">

    <div class="product-card reveal" data-category="hoodie" data-name="Hoodie Odds" data-price="Rp 320.000" data-desc="Hoodie premium dengan desain ODDS eksklusif. Bahan fleece tebal anti-angin, cocok untuk evening rides atau casual hangout." data-img="images/hoodie-odds.jpg">
      <div class="product-img-wrap">
        <div class="product-img"><img src="images/hoodie-odds.jpg" alt="Hoodie Odds" loading="lazy"/></div>
        <div class="product-badges"><span class="badge-lim">LIMITED</span><span class="badge-hot">BESTSELLER</span></div>
        <div class="product-num">01</div>
        <div class="product-hover">
          <button class="btn-detail">DETAIL</button>
          <a href="https://wa.me/6281218216022?text=Halo%20ANYDAMS!%20Saya%20mau%20order%20Hoodie%20Odds" target="_blank" class="btn-order-quick">ORDER WA &rarr;</a>
        </div>
      </div>
      <div class="product-info">
        <div class="product-cat">HOODIE</div>
        <div class="product-name">Hoodie Odds</div>
        <div class="product-foot">
          <span class="product-price">Rp 320.000</span>
          <span class="stock-badge low">3 LEFT</span>
        </div>
      </div>
    </div>

    <div class="product-card reveal delay-1" data-category="jaket" data-name="Jaket McLaren" data-price="Rp 580.000" data-desc="Jaket racing-inspired dengan detail McLaren Damsik Edition. Outer nylon tahan air, inner fleece hangat." data-img="images/jaket-mclaren.jpg">
      <div class="product-img-wrap">
        <div class="product-img"><img src="images/jaket-mclaren.jpg" alt="Jaket McLaren" loading="lazy"/></div>
        <div class="product-badges"><span class="badge-lim">EXCLUSIVE</span></div>
        <div class="product-num">02</div>
        <div class="product-hover">
          <button class="btn-detail">DETAIL</button>
          <a href="https://wa.me/6281218216022?text=Halo%20ANYDAMS!%20Saya%20mau%20order%20Jaket%20McLaren" target="_blank" class="btn-order-quick">ORDER WA &rarr;</a>
        </div>
      </div>
      <div class="product-info">
        <div class="product-cat">JAKET</div>
        <div class="product-name">Jaket McLaren</div>
        <div class="product-foot">
          <span class="product-price">Rp 580.000</span>
          <span class="stock-badge ready">READY</span>
        </div>
      </div>
    </div>

    <div class="product-card reveal delay-2" data-category="pants" data-name="Pants Gradient" data-price="Rp 290.000" data-desc="Celana gradient dye dengan cut oversized yang nyaman. Material ripstop ringan dan breathable." data-img="images/pants-gradient.jpg">
      <div class="product-img-wrap">
        <div class="product-img"><img src="images/pants-gradient.jpg" alt="Pants Gradient" loading="lazy"/></div>
        <div class="product-badges"><span class="badge-hot">NEW</span></div>
        <div class="product-num">03</div>
        <div class="product-hover">
          <button class="btn-detail">DETAIL</button>
          <a href="https://wa.me/6281218216022?text=Halo%20ANYDAMS!%20Saya%20mau%20order%20Pants%20Gradient" target="_blank" class="btn-order-quick">ORDER WA &rarr;</a>
        </div>
      </div>
      <div class="product-info">
        <div class="product-cat">PANTS</div>
        <div class="product-name">Pants Gradient</div>
        <div class="product-foot">
          <span class="product-price">Rp 290.000</span>
          <span class="stock-badge ready">READY</span>
        </div>
      </div>
    </div>

    <div class="product-card reveal" data-category="topi" data-name="Cap Marlboro" data-price="Rp 120.000" data-desc="Dad cap dengan material washed cotton dan embroidery ANYDAMS x Marlboro Damsik." data-img="images/cap-marlboro.jpg">
      <div class="product-img-wrap">
        <div class="product-img"><img src="images/cap-marlboro.jpg" alt="Cap Marlboro" loading="lazy"/></div>
        <div class="product-badges"><span class="badge-lim">LIMITED</span></div>
        <div class="product-num">04</div>
        <div class="product-hover">
          <button class="btn-detail">DETAIL</button>
          <a href="https://wa.me/6281218216022?text=Halo%20ANYDAMS!%20Saya%20mau%20order%20Cap%20Marlboro" target="_blank" class="btn-order-quick">ORDER WA &rarr;</a>
        </div>
      </div>
      <div class="product-info">
        <div class="product-cat">CAP</div>
        <div class="product-name">Cap Marlboro</div>
        <div class="product-foot">
          <span class="product-price">Rp 120.000</span>
          <span class="stock-badge low">5 LEFT</span>
        </div>
      </div>
    </div>

    <div class="product-card reveal delay-1" data-category="shoes" data-name="Shoes ASICS Damsik" data-price="Rp 750.000" data-desc="Kolaborasi ASICS x ANYDAMS Damsik Edition. GEL cushioning original, desain eksklusif limited 50 pairs." data-img="images/shoes-asics.jpg">
      <div class="product-img-wrap">
        <div class="product-img"><img src="images/shoes-asics.jpg" alt="Shoes ASICS" loading="lazy"/></div>
        <div class="product-badges"><span class="badge-lim">COLLAB</span><span class="badge-hot">50 PAIRS</span></div>
        <div class="product-num">05</div>
        <div class="product-hover">
          <button class="btn-detail">DETAIL</button>
          <a href="https://wa.me/6281218216022?text=Halo%20ANYDAMS!%20Saya%20mau%20order%20Shoes%20ASICS%20Damsik" target="_blank" class="btn-order-quick">ORDER WA &rarr;</a>
        </div>
      </div>
      <div class="product-info">
        <div class="product-cat">SHOES</div>
        <div class="product-name">Shoes ASICS Damsik</div>
        <div class="product-foot">
          <span class="product-price">Rp 750.000</span>
          <span class="stock-badge low">2 LEFT</span>
        </div>
      </div>
    </div>

    <div class="product-card reveal delay-2" data-category="tshirt" data-name="T-Shirt Guest" data-price="Rp 175.000" data-desc="Kaos oversized dengan print Guest Series. Cotton combed 30s premium, sablon rubber tahan lama." data-img="images/tshirt-guest.jpg">
      <div class="product-img-wrap">
        <div class="product-img"><img src="images/tshirt-guest.jpg" alt="T-Shirt Guest" loading="lazy"/></div>
        <div class="product-badges"><span class="badge-ready">READY STOCK</span></div>
        <div class="product-num">06</div>
        <div class="product-hover">
          <button class="btn-detail">DETAIL</button>
          <a href="https://wa.me/6281218216022?text=Halo%20ANYDAMS!%20Saya%20mau%20order%20T-Shirt%20Guest" target="_blank" class="btn-order-quick">ORDER WA &rarr;</a>
        </div>
      </div>
      <div class="product-info">
        <div class="product-cat">T-SHIRT</div>
        <div class="product-name">T-Shirt Guest</div>
        <div class="product-foot">
          <span class="product-price">Rp 175.000</span>
          <span class="stock-badge ready">READY</span>
        </div>
      </div>
    </div>

  </div>
</section>

<!-- LOOKBOOK -->
<section id="lookbook" class="lookbook">
  <div class="lookbook-header reveal">
    <div class="section-eyebrow">Lookbook</div>
    <h2 class="section-title">Style <span class="thin">Guide</span></h2>
  </div>
  <div class="lookbook-grid">
    <div class="lb-item lb-main">
      <img src="images/hoodie-odds.jpg" alt="Lookbook Main" loading="lazy"/>
      <div class="lb-caption">
        <span class="lb-tag">SS26 / LOOK 01</span>
        <span class="lb-detail">Hoodie Odds &times; Pants Gradient</span>
      </div>
    </div>
    <div class="lb-item lb-sm">
      <img src="images/jaket-mclaren.jpg" alt="Lookbook 2" loading="lazy"/>
      <div class="lb-caption">
        <span class="lb-tag">SS26 / LOOK 02</span>
        <span class="lb-detail">Jaket McLaren</span>
      </div>
    </div>
    <div class="lb-item lb-sm-b">
      <img src="images/cap-marlboro.jpg" alt="Lookbook 3" loading="lazy"/>
      <div class="lb-caption">
        <span class="lb-tag">ACCESSORIES</span>
        <span class="lb-detail">Cap Marlboro</span>
      </div>
    </div>
    <div class="lb-wide">
      <div class="lb-wide-text">
        <div class="section-eyebrow">Editorial</div>
        <p>&ldquo;Pakai apa yang kamu mau, bukan apa yang orang minta.&rdquo;</p>
        <a href="https://wa.me/6281218216022" target="_blank" class="btn-main">Order Sekarang <span class="arrow">&#x2192;</span></a>
      </div>
      <div class="lb-mid">
        <img src="images/shoes-asics.jpg" alt="Shoes ASICS" loading="lazy"/>
        <div class="lb-caption">
          <span class="lb-tag">COLLAB</span>
          <span class="lb-detail">ASICS x ANYDAMS Damsik Edition</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- TESTIMONIALS -->
<section class="testimonial-section">
  <div class="testimonial-header reveal">
    <div class="section-eyebrow">Testimonial</div>
    <h2 class="section-title">Yang Udah <span class="thin">Pake</span></h2>
  </div>
  <div class="testimonial-grid">
    <div class="testi-card reveal">
      <div class="testi-stars"><span>&#9733;</span><span>&#9733;</span><span>&#9733;</span><span>&#9733;</span><span>&#9733;</span></div>
      <p class="testi-text">&ldquo;Hoodie Odds kualitasnya beneran bagus banget. Udah 6 bulan dipake tiap hari masih kenceng jahitannya. Worth it banget bro!&rdquo;</p>
      <div class="testi-author">
        <div class="testi-avatar"><div class="testi-avatar-ph">RZ</div></div>
        <div>
          <div class="testi-name">Reza D.</div>
          <div class="testi-loc">Jakarta Selatan</div>
        </div>
      </div>
    </div>
    <div class="testi-card reveal delay-1">
      <div class="testi-stars"><span>&#9733;</span><span>&#9733;</span><span>&#9733;</span><span>&#9733;</span><span>&#9733;</span></div>
      <p class="testi-text">&ldquo;Jaket McLaren bener-bener cinematic sih. Tiap keluar pada nanya beli dimana. Response adminnya juga cepet banget pas order.&rdquo;</p>
      <div class="testi-author">
        <div class="testi-avatar"><div class="testi-avatar-ph">AN</div></div>
        <div>
          <div class="testi-name">Andi N.</div>
          <div class="testi-loc">Bandung</div>
        </div>
      </div>
    </div>
    <div class="testi-card reveal delay-2">
      <div class="testi-stars"><span>&#9733;</span><span>&#9733;</span><span>&#9733;</span><span>&#9733;</span><span>&#9733;</span></div>
      <p class="testi-text">&ldquo;ASICS Damsik Edition-nya keren parah. Gua dapet yang ke-12 dari 50. Packagingnya rapi, pengiriman cepet. Recommended!&rdquo;</p>
      <div class="testi-author">
        <div class="testi-avatar"><div class="testi-avatar-ph">FY</div></div>
        <div>
          <div class="testi-name">Fajar Y.</div>
          <div class="testi-loc">Surabaya</div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- INFO -->
<section id="info" class="info-section">
  <div class="info-header reveal">
    <div class="section-eyebrow">Info</div>
    <h2 class="section-title">Wajib <span class="thin">Tahu</span></h2>
  </div>
  <div class="info-grid">
    <div class="info-card reveal">
      <div class="info-num">01</div>
      <div class="info-icon-wrap"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M20 7H4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2z"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg></div>
      <h3>Cara Bayar</h3>
      <p>Transfer Bank / QRIS / GoPay / OVO / Dana. Konfirmasi pembayaran via WhatsApp.</p>
      <div class="info-detail">BCA / MANDIRI / GOPAY</div>
    </div>
    <div class="info-card reveal delay-1">
      <div class="info-num">02</div>
      <div class="info-icon-wrap"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><rect width="16" height="16" x="4" y="4" rx="2"/><path d="m9 12 2 2 4-4"/></svg></div>
      <h3>Ukuran</h3>
      <p>Tersedia S, M, L, XL. Size guide tersedia. Tanya admin untuk rekomendasi size yang tepat.</p>
      <div class="info-detail">SIZE S / M / L / XL</div>
    </div>
    <div class="info-card reveal delay-2">
      <div class="info-num">03</div>
      <div class="info-icon-wrap"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M5 12h14"/><path d="m12 5 7 7-7 7"/></svg></div>
      <h3>Pengiriman</h3>
      <p>Nationwide via J&amp;T / JNE / SiCepat. Khusus Jabodetabek bisa same-day. Packing rapi &amp; aman.</p>
      <div class="info-detail">1-3 HARI KERJA</div>
    </div>
    <div class="info-card reveal delay-3">
      <div class="info-num">04</div>
      <div class="info-icon-wrap"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></div>
      <h3>Garansi</h3>
      <p>Garansi kualitas 7 hari. Cacat produksi? Kami ganti. No question asked untuk manufaktur defect.</p>
      <div class="info-detail">7 HARI GARANSI</div>
    </div>
  </div>
</section>

<!-- HOW TO ORDER -->
<section class="howto">
  <div class="howto-header reveal">
    <div class="section-eyebrow">How To Order</div>
    <h2 class="section-title">Cara <span class="thin">Order</span></h2>
  </div>
  <div class="howto-steps">
    <div class="step reveal">
      <div class="step-num">01</div>
      <div class="step-icon">&#128247;</div>
      <div class="step-title">Pilih Produk</div>
      <div class="step-desc">Browse koleksi di website, pilih item yang kamu mau. Catat nama produk dan size.</div>
    </div>
    <div class="step-arrow">&#x2192;</div>
    <div class="step reveal delay-1">
      <div class="step-num">02</div>
      <div class="step-icon">&#128172;</div>
      <div class="step-title">Chat WhatsApp</div>
      <div class="step-desc">Hubungi kami via WA dengan format: Nama Produk + Size + Nama + Alamat Lengkap.</div>
    </div>
    <div class="step-arrow">&#x2192;</div>
    <div class="step reveal delay-2">
      <div class="step-num">03</div>
      <div class="step-icon">&#128179;</div>
      <div class="step-title">Bayar</div>
      <div class="step-desc">Admin kirim total harga + ongkir. Transfer ke rekening yang ditentukan dan kirim bukti.</div>
    </div>
    <div class="step-arrow">&#x2192;</div>
    <div class="step reveal delay-3">
      <div class="step-num">04</div>
      <div class="step-icon">&#128230;</div>
      <div class="step-title">Packing &amp; Kirim</div>
      <div class="step-desc">Pesanan dikemas rapi dan dikirim dalam 1-2 hari kerja. Nomor resi dikonfirmasi via WA.</div>
    </div>
  </div>
  <div class="howto-cta reveal">
    <a href="https://wa.me/6281218216022" target="_blank" class="btn-main">Chat Sekarang <span class="arrow">&#x2192;</span></a>
  </div>
</section>

<!-- FAQ -->
<section class="faq-section">
  <div class="faq-wrap">
    <div class="reveal">
      <div class="section-eyebrow">FAQ</div>
      <h2 class="section-title">Pertanyaan <span class="thin">Umum</span></h2>
      <p class="faq-sub">Masih ada pertanyaan? Langsung tanya ke WhatsApp kami, kami respon cepat.</p>
    </div>
    <div class="faq-list reveal delay-1">
      <div class="faq-item">
        <button class="faq-q">Apakah produk ANYDAMS original?<span class="faq-icon">+</span></button>
        <div class="faq-a">Ya, 100% original. Semua produk ANYDAMS dirancang dan diproduksi sendiri oleh tim kami. Tidak ada reseller atau tiruan yang kami akui.</div>
      </div>
      <div class="faq-item">
        <button class="faq-q">Berapa lama pengiriman?<span class="faq-icon">+</span></button>
        <div class="faq-a">Untuk Jabodetabek bisa same-day. Luar kota 1-3 hari kerja via J&amp;T / JNE / SiCepat. Kami konfirmasi resi setelah barang dikirim.</div>
      </div>
      <div class="faq-item">
        <button class="faq-q">Bisa tukar ukuran tidak?<span class="faq-icon">+</span></button>
        <div class="faq-a">Bisa, selama stok tersedia dan barang belum dipakai. Hubungi kami dalam 7 hari setelah barang diterima. Ongkir pengembalian ditanggung pembeli.</div>
      </div>
      <div class="faq-item">
        <button class="faq-q">Apakah ada diskon untuk pembelian bulk?<span class="faq-icon">+</span></button>
        <div class="faq-a">Ada! Untuk pembelian 5 pcs ke atas ada harga spesial. Hubungi admin via WhatsApp untuk negosiasi harga wholesale.</div>
      </div>
      <div class="faq-item">
        <button class="faq-q">Kapan drop koleksi baru?<span class="faq-icon">+</span></button>
        <div class="faq-a">Drop koleksi baru setiap 2-3 bulan. Follow Instagram @anydams.id untuk info drop pertama dan harga early bird.</div>
      </div>
    </div>
  </div>
</section>

<!-- NEWSLETTER -->
<section class="newsletter-section">
  <div class="newsletter-inner">
    <div class="newsletter-left reveal">
      <div class="section-eyebrow">Stay Updated</div>
      <h2 class="newsletter-title">Jangan<br>Ketinggalan Drop</h2>
      <p class="newsletter-sub">Daftar dan dapatkan notifikasi koleksi baru, early access, dan promo eksklusif langsung ke WA kamu.</p>
    </div>
    <div class="newsletter-right reveal delay-2">
      <form class="newsletter-form" onsubmit="handleNewsletter(event)">
        <div class="newsletter-input-wrap">
          <input type="tel" class="newsletter-input" id="newsletter-input" placeholder="+62 8xx xxxx xxxx"/>
          <button type="submit" class="newsletter-submit">DAFTAR</button>
        </div>
        <span class="newsletter-note">&#9679; No spam. Hanya info penting. Bisa unsubscribe kapanpun.</span>
      </form>
    </div>
  </div>
</section>

<!-- CTA -->
<section class="cta-section">
  <div class="cta-eyebrow reveal">Ready to order?</div>
  <h2 class="cta-title reveal delay-1">LETS<br>GO<br><span style="color:var(--accent)">DAMSIK</span></h2>
  <p class="cta-sub reveal delay-2">Pesan sekarang sebelum kehabisan. Limited stock, no restock.</p>
  <div class="cta-socials reveal delay-3">
    <a href="https://wa.me/6281218216022" target="_blank" class="social-btn wa-btn">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>
      WhatsApp Order
    </a>
    <a href="https://instagram.com/anydams.id" target="_blank" class="social-btn">&#9679; Instagram</a>
    <a href="https://tiktok.com/@anydams.id" target="_blank" class="social-btn">&#9679; TikTok</a>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <div class="footer-top-bar">
    <span class="footer-logo-big">ANYDAMS</span>
    <span class="footer-tagline">STREETWEAR JAKARTA SINCE 2023</span>
  </div>
  <div class="footer-main">
    <div class="footer-brand">
      <div class="footer-brand-logo">AD</div>
      <p>Brand streetwear lokal Jakarta yang percaya bahwa gaya adalah pernyataan, bukan seragam.</p>
      <span class="footer-badge">SS26 COLLECTION</span>
      <div class="footer-wa-btn">
        <a href="https://wa.me/6281218216022" target="_blank">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>
          +62 812-1821-6022
        </a>
      </div>
    </div>
    <div class="footer-col">
      <div class="footer-heading">Koleksi</div>
      <ul>
        <li><a href="#koleksi">Hoodie</a></li>
        <li><a href="#koleksi">Jaket</a></li>
        <li><a href="#koleksi">Pants</a></li>
        <li><a href="#koleksi">T-Shirt</a></li>
        <li><a href="#koleksi">Cap</a></li>
        <li><a href="#koleksi">Shoes</a></li>
      </ul>
    </div>
    <div class="footer-col">
      <div class="footer-heading">Info</div>
      <ul>
        <li><a href="#tentang">About Us</a></li>
        <li><a href="#info">Cara Order</a></li>
        <li><a href="#info">Pengiriman</a></li>
        <li><a href="#info">Ukuran</a></li>
        <li><span>Garansi 7 Hari</span></li>
      </ul>
    </div>
    <div class="footer-col">
      <div class="footer-heading">Sosial</div>
      <ul>
        <li><a href="https://instagram.com/anydams.id" target="_blank">Instagram</a></li>
        <li><a href="https://tiktok.com/@anydams.id" target="_blank">TikTok</a></li>
        <li><a href="https://wa.me/6281218216022" target="_blank">WhatsApp</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom">
    <span>ANYDAMS &copy; 2026. All rights reserved.</span>
    <div class="footer-socials">
      <a href="https://instagram.com/anydams.id" target="_blank">IG</a>
      <a href="https://tiktok.com/@anydams.id" target="_blank">TT</a>
      <a href="https://wa.me/6281218216022" target="_blank">WA</a>
    </div>
    <span class="footer-made">Jakarta, Indonesia</span>
  </div>
</footer>

<!-- FLOATING WA -->
<div class="float-wa" id="float-wa">
  <a href="https://wa.me/6281218216022" target="_blank" class="float-wa-btn" aria-label="Chat WhatsApp">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>
  </a>
  <span class="float-wa-label">Order via WA</span>
</div>

<!-- BACK TO TOP -->
<button id="btt" onclick="window.scrollTo({top:0,behavior:'smooth'})" aria-label="Back to top">&#8593;</button>

<!-- PRODUCT MODAL -->
<div class="modal" id="product-modal">
  <div class="modal-backdrop" id="modal-backdrop"></div>
  <div class="modal-content">
    <button class="modal-close" id="modal-close">&#x2715;</button>
    <div class="modal-body">
      <div class="modal-img-wrap">
        <div class="modal-img-bg" id="modal-img-bg">
          <div class="modal-img-ph" id="modal-img-ph">ANYDAMS</div>
        </div>
        <div class="modal-img-badge" id="modal-img-badge">LIMITED DROP</div>
      </div>
      <div class="modal-info">
        <div class="modal-breadcrumb">ANYDAMS &rsaquo; <span id="modal-cat">KOLEKSI</span></div>
        <div class="modal-title" id="modal-title">Nama Produk</div>
        <div class="modal-price" id="modal-price">Rp 0</div>
        <div class="modal-desc" id="modal-desc">Deskripsi produk.</div>
        <div class="modal-sizes-section">
          <span class="modal-sizes-label">SIZE CHART</span>
          <div id="size-table">
            <table>
              <tr><th>SIZE</th><th>CHEST</th><th>LENGTH</th><th>SHOULDER</th></tr>
              <tr><td>S</td><td>96 cm</td><td>68 cm</td><td>44 cm</td></tr>
              <tr><td>M</td><td>100 cm</td><td>70 cm</td><td>46 cm</td></tr>
              <tr><td>L</td><td>106 cm</td><td>73 cm</td><td>49 cm</td></tr>
              <tr><td>XL</td><td>112 cm</td><td>76 cm</td><td>52 cm</td></tr>
            </table>
          </div>
        </div>
        <div class="modal-actions">
          <a href="#" id="modal-wa-btn" target="_blank" class="btn-wa-main">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 0 1-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 0 1-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 0 1 2.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0 0 12.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 0 0 5.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 0 0-3.48-8.413z"/></svg>
            ORDER VIA WHATSAPP
          </a>
          <span class="modal-note">&#9679; Limited stock &#x2014; Order sekarang sebelum kehabisan</span>
        </div>
      </div>
    </div>
  </div>
</div>

<script src="script.js"></script>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html written successfully')
