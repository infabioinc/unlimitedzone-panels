import json
IMG = json.load(open('/home/claude/img/imgs.json'))

html = r'''<title>Unlimited Zone Creator Panel</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700;800;900&display=swap">
<style>
:root{
  --ink:#16151d; --ink-2:#4b4957; --ink-3:#8b8996;
  --paper:#ffffff; --paper-2:#fbf8fc; --card:#ffffff; --line:#ebe8f0;
  --pink:#ff2e72; --pink-soft:#ffe3ec; --violet:#7a3cf5; --orange:#ff6a3d; --gold:#ffc43d; --gold-ink:#3a2a05;
  --grad:linear-gradient(90deg,#ff3b5c 0%,#ff2e9a 50%,#7a3cf5 100%);
  --grad-btn:linear-gradient(135deg,#ff2e72,#c43bff);
  --grad-card:linear-gradient(160deg,#6a34f0 0%,#a63bd9 55%,#ff2e8a 100%);
  --glow:radial-gradient(60% 50% at 50% 30%,rgba(255,46,114,.14),transparent 70%),radial-gradient(40% 40% at 80% 60%,rgba(122,60,245,.12),transparent 70%);
  --shadow:0 24px 60px -24px rgba(22,21,29,.28);
  --block:#15131c; --block-fg:#fff;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --ink:#f5f3f8; --ink-2:#c9c5d3; --ink-3:#8f8b9c;
  --paper:#111019; --paper-2:#171522; --card:#1c1a27; --line:#2c2938;
  --pink-soft:#3a1a2a; --shadow:0 24px 60px -24px rgba(0,0,0,.7);
  --glow:radial-gradient(60% 50% at 50% 30%,rgba(255,46,114,.18),transparent 70%),radial-gradient(40% 40% at 80% 60%,rgba(122,60,245,.16),transparent 70%);
}}
:root[data-theme="dark"]{
  --ink:#f5f3f8; --ink-2:#c9c5d3; --ink-3:#8f8b9c;
  --paper:#111019; --paper-2:#171522; --card:#1c1a27; --line:#2c2938;
  --pink-soft:#3a1a2a; --shadow:0 24px 60px -24px rgba(0,0,0,.7);
  --glow:radial-gradient(60% 50% at 50% 30%,rgba(255,46,114,.18),transparent 70%),radial-gradient(40% 40% at 80% 60%,rgba(122,60,245,.16),transparent 70%);
}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);font-family:Montserrat,"Segoe UI",system-ui,sans-serif;font-size:16px;line-height:1.55;-webkit-font-smoothing:antialiased}
a{color:inherit;text-decoration:none}
button{font:inherit;cursor:pointer;border:0;background:none;color:inherit}
h1,h2,h3{margin:0;text-wrap:balance;line-height:1.08;letter-spacing:-.02em}
.wrap{max-width:1200px;margin:0 auto;padding:0 32px}
:focus-visible{outline:2px solid var(--pink);outline-offset:3px;border-radius:6px}
.gtext{background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}

/* nav */
.nav{position:sticky;top:0;z-index:20;background:color-mix(in srgb,var(--paper) 90%,transparent);backdrop-filter:blur(12px);border-bottom:1px solid var(--line)}
.nav .wrap{display:flex;align-items:center;justify-content:space-between;height:72px;gap:20px}
.logo img{height:40px;width:auto;display:block}
.logo .dark{display:none}
:root[data-theme="dark"] .logo .light{display:none}:root[data-theme="dark"] .logo .dark{display:block}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .logo .light{display:none}:root:not([data-theme="light"]) .logo .dark{display:block}}
.nav-actions{display:flex;align-items:center;gap:10px}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:13px 24px;border-radius:999px;font-weight:700;font-size:15px;border:1px solid var(--line);background:var(--card);color:var(--ink);transition:transform .15s,box-shadow .15s}
.btn:hover{transform:translateY(-1px);box-shadow:var(--shadow)}
.btn.primary{background:var(--grad-btn);color:#fff;border-color:transparent;box-shadow:0 12px 28px -12px #ff2e72}
.btn.ghost{background:transparent;border-color:transparent;font-weight:600}
.btn.theme{padding:9px 12px;font-size:13px;color:var(--ink-3);border-color:var(--line)}

/* fold 1 */
.hero{position:relative;text-align:center;padding:96px 0 72px;background:var(--glow)}
.hero .pill{display:inline-flex;align-items:center;gap:8px;padding:9px 18px;border-radius:999px;background:var(--pink-soft);color:var(--pink);font-weight:700;font-size:14px;margin-bottom:28px}
.hero h1{font-size:clamp(42px,6.4vw,84px);font-weight:900;max-width:16ch;margin:0 auto}
.hero p.lede{font-size:clamp(17px,1.6vw,21px);color:var(--ink-2);max-width:44rem;margin:26px auto 0}
.hero p.lede b{color:var(--ink);font-weight:800}
.hero .actions{display:flex;justify-content:center;gap:12px;flex-wrap:wrap;margin-top:34px}
.hero .actions .btn{padding:16px 30px;font-size:16px}
.anyone{margin-top:44px}
.anyone .eyebrow{font-size:12px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-3);margin-bottom:14px}
.chips{display:flex;justify-content:center;gap:10px;flex-wrap:wrap}
.chip{display:inline-flex;align-items:center;gap:8px;padding:10px 16px;border-radius:999px;border:1px solid var(--line);background:var(--card);font-weight:700;font-size:14px;color:var(--ink-2)}
.chip .av{width:26px;height:26px;border-radius:50%;overflow:hidden;flex-shrink:0;background:var(--pink-soft)}
.chip .av img{width:100%;height:100%;object-fit:cover;object-position:50% 15%;display:block}
.earn{display:grid;grid-template-columns:repeat(3,1fr);gap:0;max-width:880px;margin:52px auto 0;border:1px solid var(--line);border-radius:22px;background:var(--card);overflow:hidden;box-shadow:var(--shadow)}
.earn div{padding:22px 20px;border-right:1px solid var(--line)}
.earn div:last-child{border-right:0}
.earn b{display:block;font-size:22px;font-weight:900;letter-spacing:-.02em}
.earn span{font-size:13.5px;color:var(--ink-3);font-weight:600}

/* fold 2 */
.stats{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid var(--line);border-bottom:1px solid var(--line);padding:44px 0;text-align:center}
.stat b{display:block;font-size:44px;font-weight:900;letter-spacing:-.03em;font-variant-numeric:tabular-nums}
.stat span{color:var(--ink-3);font-weight:600;font-size:15px}
.why{padding:88px 0;text-align:center;background:var(--glow)}
.why h2{font-size:clamp(32px,4vw,48px);font-weight:900}
.why p.sub{color:var(--ink-2);font-size:18px;margin:14px auto 48px;max-width:40rem}
.cards{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;text-align:left}
.card{background:var(--card);border:1px solid var(--line);border-radius:22px;padding:28px 26px;box-shadow:0 10px 30px -22px rgba(22,21,29,.35)}
.card .ic{width:52px;height:52px;border-radius:14px;background:var(--pink-soft);color:var(--pink);display:grid;place-items:center;margin-bottom:22px}
.card h3{font-size:19px;font-weight:800;margin-bottom:10px}
.card p{margin:0;color:var(--ink-2);font-size:15px}
.creators{margin-top:56px;text-align:left}
.creators .eyebrow{font-size:12px;font-weight:800;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-3);margin-bottom:16px;text-align:center}
.crow{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.crd{display:flex;align-items:center;gap:14px;padding:16px 18px;border:1px solid var(--line);border-radius:18px;background:var(--card);transition:transform .15s,box-shadow .15s}
.crd:hover{transform:translateY(-2px);box-shadow:var(--shadow)}
.crd .av{width:56px;height:56px;border-radius:50%;overflow:hidden;flex-shrink:0;border:3px solid var(--card);box-shadow:0 0 0 2px var(--pink)}
.crd .av img{width:100%;height:100%;object-fit:cover;object-position:50% 15%;display:block}
.crd b{display:block;font-size:15px}
.crd span{font-size:13px;color:var(--ink-3)}
.crd .code{margin-left:auto;background:var(--gold);color:var(--gold-ink);font-weight:900;font-size:12px;padding:6px 10px;border-radius:8px;letter-spacing:.04em;white-space:nowrap}

/* fold 3 */
.cta-wrap{padding:72px 0 88px}
.cta{border-radius:32px;background:var(--grad);color:#fff;padding:80px 40px;text-align:center;box-shadow:var(--shadow)}
.cta h2{font-size:clamp(32px,4.4vw,52px);font-weight:900}
.cta p{color:rgba(255,255,255,.85);font-size:18px;margin:16px auto 34px;max-width:36rem}
.cta .btn{background:#fff;color:#ff2e72;border-color:transparent;padding:16px 32px;font-size:16px}
footer{border-top:1px solid var(--line);padding:28px 0 40px;color:var(--ink-3);font-size:14px}
footer .wrap{display:grid;grid-template-columns:1fr auto 1fr;align-items:center;gap:16px}
footer .links{display:flex;gap:18px;justify-content:flex-end;align-items:center}
footer .logo img{height:26px}

/* creator page */
.cp{position:relative;color:#fff;background:var(--block) center/cover no-repeat;overflow:hidden}
.cp::before{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(15,12,22,.92) 0%,rgba(15,12,22,.55) 45%,rgba(15,12,22,.35) 100%)}
.cp .wrap{position:relative;display:grid;grid-template-columns:1.05fr auto .95fr;gap:36px;align-items:center;padding-top:64px;padding-bottom:64px;min-height:640px}
.cp .chip-brand{display:inline-block;background:var(--gold);color:var(--gold-ink);font-weight:900;font-size:14px;letter-spacing:.06em;padding:9px 16px;border-radius:8px;margin-bottom:22px}
.cp h1{font-size:clamp(32px,3.6vw,50px);font-weight:900;color:#fff}
.cp h1 em{font-style:normal;color:var(--gold)}
.cp p.sub{margin:18px 0 0;color:rgba(255,255,255,.8);max-width:30rem;font-size:17px}
.portrait{width:300px;height:300px;border-radius:50%;overflow:hidden;border:7px solid #fff;box-shadow:0 30px 60px -20px rgba(0,0,0,.7);aspect-ratio:1/1;flex-shrink:0;background:var(--violet);display:grid;place-items:center;font-size:84px;font-weight:900}
.portrait img{width:100%;height:100%;object-fit:cover;object-position:50% 15%;display:block}
.phone{width:min(380px,100%);margin-left:auto;background:var(--card);color:var(--ink);border-radius:36px;box-shadow:0 40px 80px -30px rgba(0,0,0,.8);overflow:hidden}
.phone .top{background:var(--grad-card);color:#fff;padding:24px 22px 58px;clip-path:polygon(0 0,100% 0,100% 82%,0 100%)}
.phone .top .row{display:flex;justify-content:space-between;align-items:center;margin-bottom:22px}
.phone .top .bchip{background:var(--gold);color:var(--gold-ink);font-weight:900;font-size:13px;letter-spacing:.06em;padding:7px 12px;border-radius:8px}
.phone .top .stars{color:var(--gold);font-size:17px;letter-spacing:2px}
.phone .top h2{font-size:23px;font-weight:600;color:#fff;letter-spacing:0}
.phone .top h2 em{font-style:normal;color:var(--gold);font-weight:900}
.phone .top p{margin:8px 0 0;font-weight:700;font-size:15px}
.phone .body{padding:0 16px 18px;margin-top:-40px;position:relative;display:flex;flex-direction:column;gap:10px}
.info{display:flex;gap:12px;align-items:center;background:linear-gradient(90deg,#7a3cf5,#c43bff);color:#fff;border-radius:14px;padding:12px 14px}
.info .ic{width:34px;height:34px;border-radius:10px;background:rgba(255,255,255,.2);display:grid;place-items:center;flex-shrink:0}
.info small{display:block;font-size:10px;letter-spacing:.12em;text-transform:uppercase;font-weight:800;opacity:.85}
.info b{font-size:15px}
.codecard{background:var(--gold);color:var(--gold-ink);border-radius:16px;padding:16px}
.codecard small{display:block;font-size:10px;letter-spacing:.14em;text-transform:uppercase;font-weight:800;margin-bottom:6px}
.codecard b{display:block;font-size:28px;font-weight:900;letter-spacing:.02em;line-height:1}
.codecard span{display:block;font-size:11.5px;margin-top:8px;font-weight:600}
.visit{border:1px solid var(--line);border-radius:16px;padding:16px;background:var(--card)}
.visit .h{display:flex;gap:12px;align-items:center;margin-bottom:10px}
.visit .h .ic{width:42px;height:42px;border-radius:12px;background:var(--grad-btn);color:#fff;display:grid;place-items:center}
.visit .h b{display:block;font-size:16px}
.visit .h span{font-size:12.5px;color:var(--ink-3)}
.visit p{margin:0 0 12px;color:var(--ink-2);font-size:13.5px}
.visit .btn{width:100%;padding:13px}
.visit .row2{display:flex;gap:8px;margin-top:8px}
.visit .row2 .btn{font-size:13px;padding:10px}
.tabbar{display:flex;justify-content:space-around;border-top:1px solid var(--line);padding:10px 8px 14px;color:var(--ink-3);font-size:10px;font-weight:700}
.tabbar div{display:flex;flex-direction:column;align-items:center;gap:4px}
.tabbar div.on{color:var(--violet)}
.tabbar .qr{width:46px;height:46px;border-radius:50%;background:var(--grad-btn);color:#fff;display:grid;place-items:center;margin-top:-30px;border:4px solid var(--card)}

.sec{padding:72px 0}
.sec h2{font-size:32px;font-weight:900;margin-bottom:8px}
.sec p.sub{color:var(--ink-2);margin:0 0 28px}
.picks3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.pick{border:1px solid var(--line);border-radius:20px;overflow:hidden;background:var(--card)}
.pick .ph{height:260px;position:relative;background:var(--paper-2)}
.pick .ph .bg{position:absolute;inset:-20px;background-size:cover;background-position:center;filter:blur(18px) saturate(1.2);opacity:.9}
.pick .ph img{position:relative;width:100%;height:100%;object-fit:contain;display:block}
.pick .bd{padding:16px 18px 18px}
.pick .bd b{display:block;font-size:16px}
.pick .bd span{font-size:14px;color:var(--ink-2)}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.step{padding:26px;border-radius:20px;background:var(--paper-2);border:1px solid var(--line)}
.step .n{width:34px;height:34px;border-radius:50%;background:var(--grad-btn);color:#fff;display:grid;place-items:center;font-weight:900;font-size:14px;margin-bottom:14px}
.step h3{font-size:18px;font-weight:800;margin-bottom:8px}
.step p{margin:0;color:var(--ink-2);font-size:15px}
.storecard{display:grid;grid-template-columns:260px 1fr;gap:28px;border:1px solid var(--line);border-radius:24px;background:var(--card);padding:26px;align-items:center}
.storecard .ph{border-radius:16px;overflow:hidden;aspect-ratio:3/4}
.storecard .ph img{width:100%;height:100%;object-fit:cover;display:block}
.storecard dl{margin:18px 0 0;display:grid;grid-template-columns:auto 1fr;gap:8px 18px;font-size:14.5px}
.storecard dt{color:var(--ink-3);font-weight:700}.storecard dd{margin:0;font-weight:600}
.note{font-size:13px;color:var(--ink-3);margin-top:16px}
/* apply modal */
.modal{position:fixed;inset:0;z-index:50;display:none;align-items:center;justify-content:center;padding:20px;background:rgba(15,12,22,.6);backdrop-filter:blur(6px)}
.modal.open{display:flex}
.modal .box{width:min(460px,100%);background:var(--card);color:var(--ink);border-radius:26px;padding:30px 28px;box-shadow:var(--shadow);position:relative}
.modal .close{position:absolute;top:14px;right:14px;width:36px;height:36px;border-radius:50%;background:var(--paper-2);color:var(--ink-2);font-size:18px;display:grid;place-items:center}
.modal h2{font-size:26px;font-weight:900;margin-bottom:6px}
.modal p.sub{color:var(--ink-2);font-size:14.5px;margin:0 0 20px}
.field{display:flex;flex-direction:column;gap:6px;margin-bottom:14px}
.field label{font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3)}
.field input,.field select{font:inherit;font-size:15px;padding:13px 14px;border-radius:12px;border:1px solid var(--line);background:var(--paper-2);color:var(--ink);width:100%}
.field input:focus,.field select:focus{outline:2px solid var(--pink);outline-offset:0;border-color:transparent}
.modal .btn{width:100%;padding:15px;margin-top:6px}
.modal .fine{font-size:12px;color:var(--ink-3);margin:12px 0 0;text-align:center}
.modal .done{text-align:center;padding:16px 0}
.modal .done .tick{width:64px;height:64px;border-radius:50%;background:var(--grad-btn);color:#fff;display:grid;place-items:center;margin:0 auto 16px;font-size:30px;font-weight:900}
/* ===== premium layer: aurora bg, glass, micro-animations ===== */
.aurora{position:absolute;inset:0;overflow:hidden;pointer-events:none;z-index:0}
.aurora i{position:absolute;border-radius:50%;filter:blur(70px);opacity:.55;animation:drift 18s ease-in-out infinite alternate;will-change:transform}
.aurora i:nth-child(1){width:46vw;height:46vw;left:-10vw;top:-14vw;background:radial-gradient(circle,#ff2e72,transparent 65%)}
.aurora i:nth-child(2){width:40vw;height:40vw;right:-8vw;top:-6vw;background:radial-gradient(circle,#7a3cf5,transparent 65%);animation-delay:-6s;animation-duration:22s}
.aurora i:nth-child(3){width:34vw;height:34vw;left:30vw;bottom:-18vw;background:radial-gradient(circle,#ffc43d,transparent 65%);animation-delay:-11s;animation-duration:26s;opacity:.35}
.grain{position:absolute;inset:0;pointer-events:none;opacity:.06;mix-blend-mode:multiply;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
:root[data-theme="dark"] .grain{mix-blend-mode:screen;opacity:.08}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) .grain{mix-blend-mode:screen;opacity:.08}}
@keyframes drift{0%{transform:translate3d(0,0,0) scale(1)}100%{transform:translate3d(6vw,4vw,0) scale(1.15)}}
.hero,.why{position:relative;isolation:isolate}
.hero>.wrap,.why>.wrap{position:relative;z-index:1}
.hero.has-bg{background:var(--block) center/cover no-repeat;color:#fff}
.hero.has-bg::after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(15,12,22,.55),rgba(15,12,22,.85))}
.hero.has-bg .wrap{z-index:2}.hero.has-bg h1,.hero.has-bg .lede,.hero.has-bg .lede b{color:#fff}.hero.has-bg .lede{color:rgba(255,255,255,.8)}

/* glass on hover */
.card,.crd,.earn,.pick,.step,.stat,.chip{position:relative;transition:transform .35s cubic-bezier(.2,.8,.2,1),box-shadow .35s,background-color .35s,border-color .35s}
.card::before,.crd::before,.pick::before,.step::before{content:"";position:absolute;inset:0;border-radius:inherit;padding:1px;background:linear-gradient(135deg,rgba(255,46,114,.7),rgba(122,60,245,.7),rgba(255,196,61,.7));-webkit-mask:linear-gradient(#000 0 0) content-box,linear-gradient(#000 0 0);-webkit-mask-composite:xor;mask-composite:exclude;opacity:0;transition:opacity .35s;pointer-events:none}
.card:hover,.crd:hover,.pick:hover,.step:hover{transform:translateY(-6px);background:color-mix(in srgb,var(--card) 72%,transparent);backdrop-filter:blur(14px) saturate(1.4);-webkit-backdrop-filter:blur(14px) saturate(1.4);box-shadow:0 30px 60px -28px rgba(122,60,245,.45),0 0 0 1px rgba(255,255,255,.35) inset}
.card:hover::before,.crd:hover::before,.pick:hover::before,.step:hover::before{opacity:1}
.chip:hover{transform:translateY(-2px);border-color:transparent;box-shadow:0 10px 24px -14px rgba(255,46,114,.6);background:color-mix(in srgb,var(--card) 70%,transparent);backdrop-filter:blur(10px)}
.card .ic{transition:transform .35s cubic-bezier(.2,.8,.2,1),background .35s,color .35s}
.card:hover .ic{transform:rotate(-6deg) scale(1.08);background:var(--grad-btn);color:#fff}
.stat b{transition:transform .35s}.stat:hover b{transform:scale(1.06)}

/* buttons: shine sweep + press */
.btn{position:relative;overflow:hidden}
.btn.primary::after,.cta .btn::after{content:"";position:absolute;top:-40%;left:-60%;width:40%;height:180%;background:linear-gradient(120deg,transparent,rgba(255,255,255,.55),transparent);transform:skewX(-20deg);transition:left .6s ease}
.btn.primary:hover::after,.cta .btn:hover::after{left:130%}
.btn:active{transform:translateY(0) scale(.98)}
.btn.primary{background-size:200% 200%;animation:gradshift 6s ease infinite}
@keyframes gradshift{0%{background-position:0% 50%}50%{background-position:100% 50%}100%{background-position:0% 50%}}
.gtext{background-size:200% auto;animation:shimmer 5s linear infinite}
@keyframes shimmer{to{background-position:200% center}}

/* reveal on scroll (from a visible resting state) */
.rv{opacity:.35;transform:translateY(14px);transition:opacity .7s ease,transform .7s cubic-bezier(.2,.8,.2,1)}
.rv.in{opacity:1;transform:none}
.rv:nth-child(2){transition-delay:.08s}.rv:nth-child(3){transition-delay:.16s}.rv:nth-child(4){transition-delay:.24s}

/* creator page: floating phone + pulsing portrait ring */
.phone{animation:float 7s ease-in-out infinite}
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
.portrait{position:relative}
.portrait::after{content:"";position:absolute;inset:-14px;border-radius:50%;border:2px solid rgba(255,255,255,.35);animation:pulse 3s ease-out infinite}
@keyframes pulse{0%{transform:scale(.92);opacity:.9}100%{transform:scale(1.12);opacity:0}}
.info,.codecard,.visit{transition:transform .3s}.info:hover,.codecard:hover,.visit:hover{transform:translateX(3px)}
.cta{position:relative;overflow:hidden}
.cta::before{content:"";position:absolute;inset:-40%;background:conic-gradient(from 0deg,transparent 0 70%,rgba(255,255,255,.18) 80%,transparent 90%);animation:spin 14s linear infinite}
.cta>*{position:relative}
@keyframes spin{to{transform:rotate(360deg)}}
@media (prefers-reduced-motion:reduce){.aurora i,.btn.primary,.gtext,.phone,.portrait::after,.cta::before{animation:none!important}.rv{opacity:1;transform:none}}

/* credits */
footer .credits{display:flex;align-items:center;gap:10px;font-size:9.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-3);margin-left:18px;padding-left:18px;border-left:1px solid var(--line)}
footer .credits a{display:inline-flex;align-items:center;opacity:.85;transition:opacity .2s,transform .2s}
footer .credits a:hover{opacity:1;transform:translateY(-1px)}
footer .credits img{height:22px;width:auto;display:block;border-radius:3px}
footer .credits .go .dk{display:none}
:root[data-theme="dark"] footer .credits .go .lt{display:none}:root[data-theme="dark"] footer .credits .go .dk{display:block}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]) footer .credits .go .lt{display:none}:root:not([data-theme="light"]) footer .credits .go .dk{display:block}}
.toast{position:fixed;left:50%;bottom:24px;transform:translateX(-50%);background:var(--block);color:#fff;padding:10px 16px;border-radius:999px;font-size:13px;font-weight:700;opacity:0;pointer-events:none;transition:opacity .2s}
.toast.show{opacity:1}

@media (max-width:960px){
  .earn,.stats,.cards,.crow,.picks3,.steps{grid-template-columns:1fr 1fr}
  .cp .wrap{grid-template-columns:1fr;text-align:center;justify-items:center}
  .cp p.sub{margin-inline:auto}.phone{margin:0 auto}.portrait{width:220px;height:220px}
  .storecard{grid-template-columns:1fr}.storecard .ph{aspect-ratio:16/9}
  footer .wrap{grid-template-columns:1fr;text-align:center}footer .links{justify-content:center;flex-wrap:wrap}
}
@media (max-width:600px){.earn,.stats,.cards,.crow,.picks3,.steps{grid-template-columns:1fr}.earn div{border-right:0;border-bottom:1px solid var(--line)}}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
</style>

<div id="app"></div>
<div class="toast" id="toast"></div>
<div class="modal" id="applyModal" role="dialog" aria-modal="true" aria-labelledby="applyTitle">
  <div class="box">
    <button class="close" id="applyClose" aria-label="Close">×</button>
    <form id="applyForm" novalidate>
      <h2 id="applyTitle">Become a creator</h2>
      <p class="sub">Tell us who you are. We'll send your store code and your page within 24 hours.</p>
      <div class="field"><label for="f-name">Full name</label><input id="f-name" name="name" type="text" required autocomplete="name" placeholder="Riya Sharma"></div>
      <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" required autocomplete="email" placeholder="you@example.com"></div>
      <div class="field"><label for="f-phone">Phone number</label><input id="f-phone" name="phone" type="tel" required autocomplete="tel" inputmode="tel" placeholder="+91 98xxx xxxxx"></div>
      <div class="field"><label for="f-occ">Occupation</label><select id="f-occ" name="occupation" required><option value="">Select one</option><option>Mother</option><option>Father</option><option>Student</option><option>Teenager</option><option>Working professional</option><option>Content creator</option><option>Business owner</option><option>Other</option></select></div>
      <button class="btn primary" type="submit">Apply Now — It's Free</button>
      <p class="fine">No follower minimum. We'll reach you on WhatsApp or email.</p>
    </form>
    <div class="done" id="applyDone" hidden><div class="tick">✓</div><h2>You're in the queue!</h2><p class="sub">Thanks, <b id="doneName"></b>. The Unlimited Zone team will reach out within 24 hours with your store code.</p><button class="btn primary" id="applyDoneClose" type="button">Done</button></div>
  </div>
</div>

<script>
const IMG = __IMG__;
const CREATORS = [
  { slug:"riya-sharma", name:"Riya Sharma", type:"Mom & family creator", store:"Jaipur", date:"September 13, 2026", day:"Saturday", time:"02:00 PM", code:"UZ-RIYA", photo:"festivenight", avatar:"momkids",
    picks:[["momkids","Kids Corner","Everything for the little ones"],["festivestore","Family Fashion Weekend","The whole family, one bill"],["family","Puma kids' sneakers","Store-only offer with my code"]],
    headline:["Come shop the","Family Fashion Weekend","with me."],
    intro:"Weekend shopping for the whole family — kidswear, dad's denim, mom's occasion wear — under one roof in Jaipur. I'll be at the store Saturday afternoon; come say hi and use my code at billing." },
  { slug:"kabir-malhotra", name:"Kabir Malhotra", type:"Fashion & denim creator", store:"Jaipur", date:"September 20, 2026", day:"Sunday", time:"12:30 PM", code:"UZ-KABIR", photo:"store", avatar:"kabir",
    picks:[["store","Denim Edit","Levi's 511 & 501 on the rack"],["kabir","Linen & casual shirts","My weekend uniform"],["family","Athleisure","Puma and more, all sizes"]],
    headline:["What I found at","Unlimited Zone","Jaipur."],
    intro:"The Denim Edit weekend — Levi's, branded athleisure and the new-arrivals rack. I'm shooting my full haul at the store on Sunday; my code gets you the store-only offer on everything I pick." },
  { slug:"nidhi-agarwal", name:"Nidhi Agarwal", type:"College & lifestyle creator", store:"Jaipur", date:"September 27, 2026", day:"Sunday", time:"04:00 PM", code:"UZ-NIDHI", photo:"festivestore", avatar:"sage",
    picks:[["sage","Pre-draped sarees","Festive styling, done easy"],["maroon","Occasion wear","Lehenga and cape sets"],["ethnic","Sharara sets","Wedding-season edit"]],
    headline:["Festive styling,","Kids Sunday","and 100+ brands."],
    intro:"Festive season starts here — occasion wear, footwear and the Kids Sunday event. Bring the family, show my code at billing, and get the store-exclusive festive offer." },
];
const $=(s)=>document.querySelector(s);
const esc=(s)=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));
const I={
  cal:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="4" width="18" height="18" rx="3"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
  clock:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
  pin:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 21s7-6 7-11a7 7 0 1 0-14 0c0 5 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>',
  bag:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 8h12l1 13H5L6 8z"/><path d="M9 8V6a3 3 0 0 1 6 0v2"/></svg>',
  star:'<svg width="15" height="15" viewBox="0 0 24 24" fill="currentColor"><path d="M12 2l3 7 7 .6-5.3 4.6L18.5 22 12 18.3 5.5 22l1.8-7.8L2 9.6 9 9z"/></svg>',
  arrow:'<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
  qr:'<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><path d="M14 14h3v3M21 14v7h-7"/></svg>',
  home:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 11l9-8 9 8v10H3z"/></svg>',
  ticket:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 8a2 2 0 0 0 0 8v3h18v-3a2 2 0 0 1 0-8V5H3z"/></svg>',
  user:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>',
  bolt:'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 2L4 14h6l-1 8 9-12h-6z"/></svg>',
  chart:'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg>',
  cash:'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="6" width="20" height="12" rx="2"/><circle cx="12" cy="12" r="3"/></svg>',
  people:'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="9" cy="8" r="3.5"/><path d="M2 20a7 7 0 0 1 14 0M16 4a3.5 3.5 0 0 1 0 7M22 20a7 7 0 0 0-5-6.7"/></svg>',
};
const logo=`<a class="logo" href="#/"><img class="light" src="${IMG.logo}" alt="Unlimited Zone — Complete Family Wear"><img class="dark" src="${IMG.logoWhite}" alt="Unlimited Zone — Complete Family Wear"></a>`;
const nav=()=>`<div class="nav"><div class="wrap">${logo}<div class="nav-actions"><button class="btn theme" id="themeBtn" aria-label="Switch light / dark">☀︎ / ☾</button><a class="btn ghost" href="#/" data-toast="Creator login opens here once the panel is live">Login</a><a class="btn primary" href="#/" data-apply>Join Now</a></div></div></div>`;
const footer=()=>`<footer><div class="wrap">${logo}<span>© 2026 Unlimited Zone · A unit of Shyam Retail Stores. All rights reserved.</span><div class="links"><a href="#/">Privacy</a><a href="#/">Terms</a><a href="#/">Support</a><span class="credits">Site by <a href="https://fabulousmedia.in" target="_blank" rel="noopener" title="Fabulous Media"><img src="${IMG.fmLogo}" alt="Fabulous Media"></a><a class="go" href="https://gocommercially.com" target="_blank" rel="noopener" title="GoCommercially"><img class="lt" src="${IMG.goLogo}" alt="GoCommercially"><img class="dk" src="${IMG.goLogoWhite}" alt=""></a></span></div></div></footer>`;

const AVS=["momkids","kabir","sage","family","festivestore"];
function landing(){
  return `${nav()}
  <section class="hero${IMG.heroBg?" has-bg":""}" style="${IMG.heroBg?`background-image:url(${IMG.heroBg})`:""}"><div class="aurora"><i></i><i></i><i></i></div><div class="grain"></div><div class="wrap">
    <div class="pill">${I.star} Unlimited Zone Creator Programme · Jaipur first</div>
    <h1>Turn Your Influence Into <span class="gtext">Store Footfall.</span></h1>
    <p class="lede">Partner with Unlimited Zone — 100+ brands for men, women and kids under one roof — and get your own store code. <b>The more people shop with your code, the more you earn.</b> Every visit is tracked at the billing counter.</p>
    <div class="actions"><a class="btn primary" href="#/" data-apply>Become a Creator ${I.arrow}</a><a class="btn" href="#/creator/riya-sharma">See a creator page ${I.arrow}</a></div>
    <div class="anyone"><div class="eyebrow">You can be anyone</div>
      <div class="chips">${[["Mothers","momkids"],["Fathers","family"],["Kids","festivestore"],["Students","sage"],["Teenagers","kabir"]].map(([t,k])=>`<span class="chip"><span class="av"><img src="${IMG[k]}" alt=""></span>${t}</span>`).join("")}</div>
    </div>
    <div class="earn">
      <div><b>Your own code</b><span>e.g. UZ-RIYA — shared on your page and posts</span></div>
      <div><b>Earn on every bill</b><span>Commission on every bill that carries your code</span></div>
      <div><b>No follower minimum</b><span>Your city and your circle matter more than numbers</span></div>
    </div>
  </div></section>

  <section><div class="wrap"><div class="stats">
    <div class="stat rv"><b class="gtext">7</b><span>Stores across Haryana &amp; Rajasthan</span></div>
    <div class="stat rv"><b class="gtext">100+</b><span>Brands under one roof</span></div>
    <div class="stat rv"><b class="gtext">25 yrs</b><span>Family retail legacy</span></div>
    <div class="stat rv"><b class="gtext">10%</b><span>Commission on tracked bills</span></div>
  </div></div></section>

  <section class="why"><div class="aurora"><i></i><i></i><i></i></div><div class="grain"></div><div class="wrap">
    <h2>Why partner with <span class="gtext">Unlimited Zone</span>?</h2>
    <p class="sub">Everything you need to turn your audience into store visits — and get paid for every one of them.</p>
    <div class="cards">
      <div class="card rv"><div class="ic">${I.bolt}</div><h3>Your code in a day</h3><p>Apply, get approved, and receive your store code and a page like this one within 24 hours.</p></div>
      <div class="card rv"><div class="ic">${I.chart}</div><h3>Tracked at billing</h3><p>Every bill with your code is tagged at the counter. See visits, bills and what your audience buys.</p></div>
      <div class="card rv"><div class="ic">${I.cash}</div><h3>Monthly payouts</h3><p>Commission on every tracked bill, paid monthly to your account. Bonuses on event weekends.</p></div>
      <div class="card rv"><div class="ic">${I.people}</div><h3>A store team behind you</h3><p>A store manager as your contact, early access to new arrivals, and invites to store events.</p></div>
    </div>
    <div class="creators"><div class="eyebrow">Creators shopping with us this month</div>
      <div class="crow">${CREATORS.map(c=>`<a class="crd rv" href="#/creator/${c.slug}"><span class="av"><img src="${IMG[c.avatar]}" alt=""></span><span><b>${esc(c.name)}</b><span>${esc(c.type)} · ${esc(c.store)}</span></span><span class="code">${c.code}</span></a>`).join("")}</div>
    </div>
  </div></section>

  <section class="cta-wrap"><div class="wrap"><div class="cta">
    <h2>Ready to start earning?</h2>
    <p>Join the Unlimited Zone creators in Jaipur. It takes less than 2 minutes to apply — no follower minimum.</p>
    <a class="btn" href="#/" data-apply>Apply Now — It's Free ${I.arrow}</a>
  </div></div></section>
  ${footer()}`;
}

function creatorPage(c){
  const others=CREATORS.filter(x=>x.slug!==c.slug);
  return `${nav()}
  <section class="cp" style="background-image:url(${IMG[c.photo]})"><div class="wrap">
    <div>
      <div class="chip-brand">UNLIMITED ZONE • ${c.store.toUpperCase()}</div>
      <h1>${esc(c.headline[0])}<br><em>${esc(c.headline[1])}</em><br>${esc(c.headline[2])}</h1>
      <p class="sub">${esc(c.intro)}</p>
    </div>
    <div class="portrait">${c.avatar?`<img src="${IMG[c.avatar]}" alt="${esc(c.name)}">`:c.name[0]}</div>
    <div class="phone">
      <div class="top">
        <div class="row"><div class="bchip">UNLIMITED ZONE</div><div class="stars">★★★</div></div>
        <h2>Hi, I'm <em>${esc(c.name)}</em>.</h2>
        <p>I'm shopping at Unlimited Zone ${esc(c.store)} on:</p>
      </div>
      <div class="body">
        <div class="info"><div class="ic">${I.cal}</div><div><small>Date &amp; day</small><b>${esc(c.date)} • ${esc(c.day)}</b></div></div>
        <div class="info"><div class="ic">${I.clock}</div><div><small>Arrival time</small><b>${esc(c.time)}</b></div></div>
        <div class="codecard"><small>My exclusive store code</small><b>${c.code}</b><span>Show this code at billing for my store-only offer.</span></div>
        <div class="visit">
          <div class="h"><div class="ic">${I.bag}</div><div><b>Plan your visit</b><span>Shop with ${esc(c.name.split(" ")[0])} at Unlimited Zone ${esc(c.store)}</span></div></div>
          <p>Come shop with me — men, women and kids under one roof. Use my code at the counter; offer valid in store only.</p>
          <button class="btn primary" data-toast="Opens Google Maps directions to the ${esc(c.store)} store">Get directions ${I.arrow}</button>
          <div class="row2"><button class="btn" data-toast="Opens WhatsApp chat with the ${esc(c.store)} store">WhatsApp the store</button><button class="btn" data-copy="${c.code}">Copy my code</button></div>
        </div>
      </div>
      <div class="tabbar"><div class="on">${I.home}Home</div><div>${I.ticket}Offers</div><div class="qr">${I.qr}</div><div>${I.cal}Events</div><div>${I.user}Profile</div></div>
    </div>
  </div></section>

  <section class="sec"><div class="wrap">
    <h2>What I'm picking up</h2><p class="sub">${esc(c.name.split(" ")[0])}'s edit from the ${esc(c.store)} store this weekend.</p>
    <div class="picks3">${c.picks.map(([k,t,d])=>`<div class="pick rv"><div class="ph"><div class="bg" style="background-image:url(${IMG[k]})"></div><img src="${IMG[k]}" alt="${esc(t)}"></div><div class="bd"><b>${esc(t)}</b><span>${esc(d)}</span></div></div>`).join("")}</div>
  </div></section>

  <section class="sec" style="padding-top:0"><div class="wrap">
    <h2>How my code works</h2><p class="sub">Three steps. The more people use it, the more I earn — and the better the offer gets.</p>
    <div class="steps">
      <div class="step rv"><div class="n">1</div><h3>Visit Unlimited Zone ${esc(c.store)}</h3><p>Any day — or come ${esc(c.day)} from ${esc(c.time)} to shop with me.</p></div>
      <div class="step rv"><div class="n">2</div><h3>Show ${c.code} at billing</h3><p>The counter tags your bill with my code and applies the store-only offer.</p></div>
      <div class="step rv"><div class="n">3</div><h3>Tag me in your haul</h3><p>Post your finds with #UnlimitedZone${esc(c.store)} — I share the best ones.</p></div>
    </div>
  </div></section>

  <section class="sec" style="padding-top:0"><div class="wrap">
    <div class="storecard">
      <div class="ph"><img src="${IMG.front}" alt="Unlimited Zone storefront"></div>
      <div><h2 style="font-size:26px">Unlimited Zone, ${esc(c.store)}</h2><p class="sub" style="margin:0">15,000 sq ft of men's, women's, kids' and infant wear, footwear, accessories and lifestyle — Levi's, Puma and 100+ national and global brands at family-friendly prices.</p>
      <dl><dt>Offer</dt><dd>Store-only, valid with code ${c.code} at billing</dd><dt>Best time</dt><dd>${esc(c.day)}, ${esc(c.time)} onwards</dd><dt>Directions</dt><dd>Google Maps · "Unlimited Zone ${esc(c.store)}"</dd><dt>Contact</dt><dd>WhatsApp the store from the card above</dd></dl></div>
    </div>
    <div class="note">Sample page for the Jaipur creator pilot — names, dates and offers are placeholders. Other sample creators: ${others.map(o=>`<a href="#/creator/${o.slug}" style="color:var(--pink);font-weight:700">${esc(o.name)}</a>`).join(", ")} · <a href="#/" style="font-weight:700">Back to the programme</a></div>
  </div></section>
  ${footer()}`;
}

function render(){
  const m=(location.hash||"#/").match(/^#\/creator\/([a-z0-9-]+)/);
  const c=m&&CREATORS.find(x=>x.slug===m[1]);
  $("#app").innerHTML=c?creatorPage(c):landing();
  document.title=c?`${c.name} × Unlimited Zone`:"Unlimited Zone Creator Panel";
  window.scrollTo(0,0);
  const io=new IntersectionObserver((es)=>{es.forEach(e=>{if(e.isIntersecting){e.target.classList.add("in");io.unobserve(e.target);}})},{threshold:.15});
  document.querySelectorAll(".rv").forEach(el=>io.observe(el));
  document.querySelectorAll(".stat b").forEach(b=>{const m=b.textContent.match(/^(\d+)(.*)$/); if(!m) return; const n=+m[1], suf=m[2]; let t0=null; const step=(t)=>{if(!t0)t0=t; const k=Math.min(1,(t-t0)/900); b.textContent=Math.round(n*(1-Math.pow(1-k,3)))+suf; if(k<1) requestAnimationFrame(step);}; requestAnimationFrame(step);});
}
function applyTheme(t){ if(t) document.documentElement.setAttribute("data-theme",t); else document.documentElement.removeAttribute("data-theme"); }
try{ applyTheme(localStorage.getItem("uz-theme")); }catch(_){}
let tt; function toast(msg){ const t=$("#toast"); t.textContent=msg; t.classList.add("show"); clearTimeout(tt); tt=setTimeout(()=>t.classList.remove("show"),2200); }
document.addEventListener("click",(e)=>{
  if(e.target.closest("#themeBtn")){ const cur=document.documentElement.getAttribute("data-theme")||(matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light"); const next=cur==="dark"?"light":"dark"; applyTheme(next); try{localStorage.setItem("uz-theme",next);}catch(_){} return; }
  const el=e.target.closest("[data-toast],[data-copy]"); if(!el) return; e.preventDefault();
  if(el.dataset.copy){ try{navigator.clipboard.writeText(el.dataset.copy);}catch(_){} toast(`Copied ${el.dataset.copy}`); } else toast(el.dataset.toast);
});
const modal=$("#applyModal"), form=$("#applyForm"), done=$("#applyDone");
function openApply(){ form.hidden=false; done.hidden=true; form.reset(); modal.classList.add("open"); setTimeout(()=>$("#f-name").focus(),50); }
function closeApply(){ modal.classList.remove("open"); }
document.addEventListener("click",(e)=>{ const a=e.target.closest("[data-apply]"); if(a){ e.preventDefault(); openApply(); } if(e.target.closest("#applyClose,#applyDoneClose")||e.target===modal) closeApply(); });
document.addEventListener("keydown",(e)=>{ if(e.key==="Escape") closeApply(); });
form.addEventListener("submit",(e)=>{
  e.preventDefault();
  const d=Object.fromEntries(new FormData(form).entries());
  const bad=[...form.querySelectorAll("input,select")].find(i=>!i.checkValidity());
  if(bad){ bad.focus(); toast(bad.name==="email"?"Please enter a valid email":bad.name==="phone"?"Please enter your phone number":"Please fill in "+bad.name); return; }
  const list=(()=>{try{return JSON.parse(localStorage.getItem("uz-applications")||"[]")}catch(_){return []}})();
  list.push(Object.assign({at:new Date().toISOString(),page:location.hash},d));
  try{ localStorage.setItem("uz-applications",JSON.stringify(list)); }catch(_){}
  window.dispatchEvent(new CustomEvent("uz:apply",{detail:d}));
  $("#doneName").textContent=d.name.split(" ")[0]; form.hidden=true; done.hidden=false;
});
window.addEventListener("hashchange",render); render();
</script>
'''
open('/home/claude/uz-influencer-panel.html','w').write(html.replace('__IMG__', json.dumps(IMG)))
print('ok')
